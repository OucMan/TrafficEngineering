# coding:utf-8
from pytun import TunTapDevice, IFF_TUN, IFF_NO_PI
from scapy.all import *
from concurrent import futures
import grpc
import ifaceinfo_v2_pb2
import ifaceinfo_v2_pb2_grpc
import netifaces
import json
import argparse
import time
import os


def get_interfaces(router):
    res = []
    all_interfaces = netifaces.interfaces()
    for inf in all_interfaces:
        if router in inf:
            res.append(inf)
    return res


def get_adapter_info(device):
    interfaces = get_interfaces(device)
    res = []

    for inface in interfaces:
        ipv6_addr = netifaces.ifaddresses(inface)[netifaces.AF_INET6][0]['addr'].split('%')[0]
        ipv6_mask = netifaces.ifaddresses(inface)[netifaces.AF_INET6][0]['netmask']
        mac_addr = netifaces.ifaddresses(inface)[netifaces.AF_PACKET][0]['addr']
        if ipv6_addr.startswith('fe80'):
            ipv6_addr = netifaces.ifaddresses(inface)[netifaces.AF_INET][0]['addr'].split('%')[0]
            ipv6_mask = netifaces.ifaddresses(inface)[netifaces.AF_INET][0]['netmask']
        address = ifaceinfo_v2_pb2.Address(
            iface_name=inface, ipv6=ipv6_addr, mask=ipv6_mask, mac=mac_addr
        )
        res.append(address)
    return res


def get_address(device, db):
    for address in db:
        if address.iface_name == device:
            return address
    return None


class IfaceInfo(ifaceinfo_v2_pb2_grpc.IfaceInfoServicer):
    def __init__(self, device):
        self.device = device
        self.db = get_adapter_info(device)
        self.buffers = []  # save pachet in message
        self.buffer_length_threshold = 100

    def GetOneInfo(self, request, context):
        iface_name = request.name
        address = get_address(iface_name, self.db)
        if not address:
            return ifaceinfo_v2_pb2.Address(iface_name=iface_name, ipv6=None, mask=None, mac=None)
        else:
            return address

    def GetAllInfo(self, request, context):
        iface_name = request.name
        if iface_name == 'all':
            for address in self.db:
                yield address

    def SendCmd(self, request, context):
        cmd = request.cmd
        print(cmd)
        res = os.system(cmd)
        if res == 0:
            return ifaceinfo_v2_pb2.Response(type=1, resp='Succceed')
        else:
            return ifaceinfo_v2_pb2.Response(type=2, resp='Failed')

    def GetTask(self, request, context):
        while self.buffers:
            yield self.buffers.pop(0)

    def AddTask(self, device, src, dst):
        if len(self.buffers) > self.buffer_length_threshold:
            return
        self.buffers.append(ifaceinfo_v2_pb2.PacketIn(device=device, src=src, dst=dst))


def serve(device, ipv4_address, tun_device):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    s = IfaceInfo(device)
    ifaceinfo_v2_pb2_grpc.add_IfaceInfoServicer_to_server(s, server)
    server.add_insecure_port(ipv4_address)
    server.start()
    try:
        while True:
            buf = tun.read(tun.mtu)
            pkt = IP(buf)
            # paser the packet
            src_ip, dst_ip = pkt.src, pkt.dst
            if src_ip == '0.0.0.0':
                continue
            print(src_ip, dst_ip)
            s.AddTask(device, src_ip, dst_ip)

    except KeyboardInterrupt:
        server.stop(0)


def create_tun(tun_name):
    tun = TunTapDevice(name=tun_name, flags=(IFF_TUN | IFF_NO_PI))
    tun.addr = '10.6.0.1'
    tun.dstaddr = '0.0.0.0'
    tun.netmask = '0.0.0.0'
    tun.mtu = 1500
    '''
    res = os.system('route add default gw' + ' 10.6.0.1 ' + tun_name)
    if res == 0:
        return tun
    else:
        return None'''

    return tun


def default_route(tun):
    return os.system('route add default gw ' + tun.addr + ' ' + tun.name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--node", type=str, required=True, help="device name")
    parser.add_argument("--address", type=str, required=True, help="gRpc server address")
    router_name = parser.parse_args().node
    server_address = parser.parse_args().address

    tun = create_tun('packet_in')
    tun.persist(True)
    tun.up()

    if tun:
        res = default_route(tun)
        if res != 0:
            exit(1)

    serve(router_name, server_address, tun)
