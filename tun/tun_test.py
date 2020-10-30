# coding:utf-8
from pytun import TunTapDevice, IFF_TUN, IFF_NO_PI
from scapy.all import *

tun = TunTapDevice(name='packet_in', flags=(IFF_TUN | IFF_NO_PI))

tun.addr = '10.8.0.1'
tun.dstaddr = '10.8.0.2'
tun.netmask = '255.255.255.0'
tun.mtu = 1500

tun.persist(True)
tun.up()

while True:
    buf = tun.read(tun.mtu)
    pkt = IP(buf)
    # paser the packet
    src_ip, dst_ip = pkt.src, pkt.dst
    if src_ip == '0.0.0.0':
        continue
    print(src_ip, dst_ip)
