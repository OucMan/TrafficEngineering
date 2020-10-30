# 一、使用python中的第三方库pytun来创建和操作linux tun设备
  
  1. 安装pytun
  
  sudo pip install python-pytun
  
  详情见https://pypi.org/project/python-pytun/2.2.1/
  
  2. 创建tun设备，简要代码如下
  
  
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

  在路由器中运行代码，系统中会生成一个名为‘packet_in’的tun设备，同时路由表中新增一个路由表项，目的地址网段10.8.0.0/24，输出端口为packet_in设备
  
  注：查看路由命令ip route， 查看tun设备的命令 ip tuntap
  
  3. 外部设备使用scapy伪造数据包（dst_ip为10.8.0.0/24中的一个，dst_mac为路由器的接入端口的mac地址）输入到路由器中，就可以看到数据包匹配到路由表项进而转入到tun设备中，然后输出出来
  
# 二、实现packet-in机制

在grpc server中加入创建和管理tun设备的代码，然后增加默认路由，将数据包转发至tun设备，然后程序读取数据包的首部字段（src_ip和dst_ip），利用grpc发送给控制器，因此grpc应该是双向的，至此控制网络完成
  
  
  

