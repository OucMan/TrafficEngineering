# 启动拓扑

```Bash
sudo python Topo.py
```
Topo.py代码主要执行的动作有：创建4个路由器与3个主机，并设置静态路由；创建设备之间的链路；对于路由器来说，增加loopback接口，并将其设置为SR中的设备segment，同时设置所有的接口支持SRv6。形成的拓扑图如Topo_No_Controller.png所示。

# 路由器配置

## R1

R1路由器执行两个动作。第一，将去往10.0.2.0/24的Ipv4数据包封装入SRv6，并将R3和R4的Segment添加进SRH；第二，对回程数据包，即去往主机a的数据包进行Ipv6解封装，即剥离Ipv6首部，将Ipv4数据包发送给主机a。

上述两个动作对应了SRv6的两个操作。

T.Encaps: 该操作在中转节点（即数据包经过的支持SRv6的路由器，但节点本身不在Segment列表中）上执行，会在数据包外层新加一个IPv6报头以及SRH报头，并可以定义新的Segment列表，数据包将首先按照新IPv6报头中的SRH进行转发。

End.DX4: 该操作要求Segment Left为0且数据包内封装了IPv4数据包，会去掉外层的IPv6报头，并将内部的IPv4数据包转发给指定的下一跳地址。相当于VPNv4 Per-CE标签。

配置命令如下
```Bash
ip route add 10.0.2.0/24 encap seg6 mode encap  segs fc00:3::bb,fc00:4::bb dev r1-eth0
ip -6 route add fc00:1::bb/128 encap seg6local action End.DX4 nh4 10.0.0.1 dev r1-eth2
```

## R3

R3在接收到SRv6数据包后，查看到当前的Active Segment（或者目的Ipv6地址）是它自己，则需要将Segment Left减1，并更新IPv6 目的地址为当前Segment Left指定的Segment。因此需要在R3路由器上配置End操作。

配置命令如下
```Bash
ip -6 route add fc00:3::bb/128 encap seg6local action End dev r3-eth1
```
## R4

R4路由器执行两个动作。第一，对去往主机b的SRv6数据包进行Ipv6解封装，即剥离Ipv6首部，将Ipv4数据包发送给主机b；第二，将去往10.0.0.0/24的Ipv4数据包封装入SRv6，并将R1的Segment添加进SRH；

上述两个动作对应了SRv6的两个操作:

End.DX4: 该操作要求Segment Left为0且数据包内封装了IPv4数据包，会去掉外层的IPv6报头，并将内部的IPv4数据包转发给指定的下一跳地址。相当于VPNv4 Per-CE标签。

T.Encaps: 该操作在中转节点（即数据包经过的支持SRv6的路由器，但节点本身不在Segment列表中）上执行，会在数据包外层新加一个IPv6报头以及SRH报头，并可以定义新的Segment列表，数据包将首先按照新IPv6报头中的SRH进行转发。
```Bash
ip -6 route add fc00:4::bb/128 encap seg6local action End.DX4 nh4 10.0.2.1 dev r4-eth3
ip route add 10.0.0.0/24 encap seg6 mode encap  segs fc00:1::bb dev r4-eth1
```
# 关闭反向路径检测机制

进行上述配置完，并不能完成转发，原因在于Linux默认开启的反向路径检测机制，因此我们需要对路由器进行配置，即配置/proc/sys/net/ipv4/conf/下所有端口文件夹下的rp_filter文件（运行echo 0 >>rp_filter命令）。

以r4路由器举例，
```Bash
root@ubuntu:/proc/sys/net/ipv4/conf# ls
all  default  lo  r4-eth0  r4-eth1  r4-eth2  r4-eth3  r4-eth4
root@ubuntu:/proc/sys/net/ipv4/conf# cd r4-eth0
root@ubuntu:/proc/sys/net/ipv4/conf/r4-eth0# echo 0 >> rp_filter 
root@ubuntu:/proc/sys/net/ipv4/conf/r4-eth0# cd ..
root@ubuntu:/proc/sys/net/ipv4/conf# cd r4-eth1
root@ubuntu:/proc/sys/net/ipv4/conf/r4-eth1# echo 0 >> rp_filter 
root@ubuntu:/proc/sys/net/ipv4/conf/r4-eth1# cd ..
root@ubuntu:/proc/sys/net/ipv4/conf# cd r4-eth2
root@ubuntu:/proc/sys/net/ipv4/conf/r4-eth2# echo 0 >> rp_filter 
root@ubuntu:/proc/sys/net/ipv4/conf/r4-eth2# cd ..
root@ubuntu:/proc/sys/net/ipv4/conf# cd r4-eth3
root@ubuntu:/proc/sys/net/ipv4/conf/r4-eth3# echo 0 >> rp_filter 
root@ubuntu:/proc/sys/net/ipv4/conf/r4-eth3# cd ..
root@ubuntu:/proc/sys/net/ipv4/conf# cd r4-eth4
root@ubuntu:/proc/sys/net/ipv4/conf/r4-eth4# echo 0 >> rp_filter 
root@ubuntu:/proc/sys/net/ipv4/conf/r4-eth4# cd ..
root@ubuntu:/proc/sys/net/ipv4/conf# cd all
root@ubuntu:/proc/sys/net/ipv4/conf/all# echo 0 >> rp_filter 
root@ubuntu:/proc/sys/net/ipv4/conf/all# 
```
# 结果:blush:

完成上述所有配置后，即可主机A和主机B即可ping通，结果见Result1.png和Result2.png




