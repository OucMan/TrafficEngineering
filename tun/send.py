# coding:utf-8
import random
import time
from scapy.all import *


while True:
    pkt = Ether(dst='da:3f:80:55:3d:43', src='9a:6b:0c:54:14:33') / IP(src='10.0.0.1', dst='10.8.0.5') / ICMP()
    sendp(pkt, iface='a-eth0')
    time.sleep(3)
