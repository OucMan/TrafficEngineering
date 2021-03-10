# 基于SDN与SRv6的流量工程

## 概述

数据平面为IPv6网络，且支持SRv6，其实现采用的是Linux内核，采用SDN架构，构建一个集中式的控制平面，用来获得全网拓扑，计算最优路径，并下发Segment List至入口交换机。在控制器与路由器交互的过程中，我们采用了gRPC机制。整个项目采用Python 2.7

备注：整个架构中，包括两个网络，一个是路由器之间的IPv6数据平面网络，另一个是控制器与路由器之间的控制网络，因为实验是在一台机器上进行，因此我们将不同的设备放到不用的网络命名空间内，并通过创建veth pair的方式来实现控制器与路由器之间的通信。

网络拓扑

![image](https://github.com/OucMan/TrafficEngineering/blob/main/version/1/Topo.png)


## 版本

本项目包括三个版本，第一个版本为无控制器，只实现SRv6路由机制，第二个版本为有控制器，主动下发路由，第三个版本为有控制器，响应式下发路由。代码见version文件夹。


## 目录概述

control-network：路由器和控制器之间创建veth-pair，并完成通信的过程

future-work：未来工作，主要是基于Raft协议以集群形式实现高可用、可伸缩的控制平面

grpc：gRpc通信框架的实现实例

netadapter：获得网卡信息的实现实例

tun：创建并操作tun设备的实现实例

version：项目最终完整代码
