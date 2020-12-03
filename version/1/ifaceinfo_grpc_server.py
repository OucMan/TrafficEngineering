# coding:utf-8
from concurrent import futures
import grpc
import ifaceinfo_pb2
import ifaceinfo_pb2_grpc
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
        address = ifaceinfo_pb2.Address(
            iface_name=inface, ipv6=ipv6_addr, mask=ipv6_mask, mac=mac_addr
        )
        res.append(address)
    return res


def get_address(device, db):
    for address in db:
        if address.iface_name == device:
            return address
    return None


class IfaceInfo(ifaceinfo_pb2_grpc.IfaceInfoServicer):
    def __init__(self, device):
        self.device = device
        self.db = get_adapter_info(device)

    def GetOneInfo(self, request, context):
        iface_name = request.name
        address = get_address(iface_name, self.db)
        if not address:
            return ifaceinfo_pb2.Address(iface_name=iface_name, ipv6=None, mask=None, mac=None)
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
            return ifaceinfo_pb2.Response(type=1, resp='Succceed')
        else:
            return ifaceinfo_pb2.Response(type=2, resp='Failed')


def serve(device, ipv4_address):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ifaceinfo_pb2_grpc.add_IfaceInfoServicer_to_server(IfaceInfo(device), server)
    server.add_insecure_port(ipv4_address)
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--node", type=str, required=True, help="device name")
    parser.add_argument("--address", type=str, required=True, help="gRpc server address")
    router_name = parser.parse_args().node
    server_address = parser.parse_args().address
    serve(router_name, server_address)
