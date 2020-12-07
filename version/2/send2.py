# coding:utf-8
import random
import time
from scapy.all import *


while True:
    pkt = Ether(dst='0a:84:bb:ad:48:5a', src='22:d8:13:4c:94:ad') / IP(src='10.0.2.1', dst='10.0.4.1') / ICMP()
    sendp(pkt, iface='b-eth0')
    time.sleep(3)
