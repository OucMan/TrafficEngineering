# coding:utf-8
import random
import time
from scapy.all import *


while True:
    pkt = Ether(dst='d2:b3:c1:3f:68:a0', src='9a:6b:0c:54:14:33') / IP(src='10.0.0.1', dst='10.0.3.1') / ICMP()
    sendp(pkt, iface='a-eth0')
    time.sleep(3)
