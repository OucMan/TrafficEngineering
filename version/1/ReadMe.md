# 有控制器模式（主动式路由下发）

在版本０基础上，增加控制器，控制器实现的功能如下：获取实时网络拓扑，利用最短路径算法得到转发路径，主动下发路由规则到路由器。

## 拓扑

数据面拓扑和版本0一致，控制通路使用veth pair来实现，完整拓扑见Topo.png。

路由器与控制器之间的Veth Pair设置如下

```Bash
Br-R1: Veth0(10.1.1.1/24)<->Veth1(10.1.1.2/24)
Br-R2: Veth2(10.1.1.3/24)<->Veth3(10.1.1.4/24)
Br-R3: Veth4(10.1.1.5/24)<->Veth5(10.1.1.6/24)
Br-R4: Veth6(10.1.1.7/24)<->Veth7(10.1.1.8/24)
```

控制器与路由器之间的通信使用gRpc机制

## 创建控制通路

以R1为例，创建R1与控制器之间的控制通道，其余通道同理

### Root命名空间创建br0网桥（创建一次就好）

```Bash
sudo ip link add name br0 type bridge
```


### 查看R1进程号

```Bash
ps -ef | grep mininet
root      19314  19309  0 04:10 pts/11   00:00:00 bash --norc -is mininet:a
root      19316  19309  0 04:10 pts/12   00:00:00 bash --norc -is mininet:b
root      19318  19309  0 04:10 pts/20   00:00:00 bash --norc -is mininet:c
root      19320  19309  0 04:10 pts/21   00:00:00 bash --norc -is mininet:r1
root      19322  19309  0 04:10 pts/22   00:00:00 bash --norc -is mininet:r2
root      19324  19309  0 04:10 pts/23   00:00:00 bash --norc -is mininet:r3
root      19326  19309  0 04:10 pts/24   00:00:00 bash --norc -is mininet:r4
xxx+  19572  19559  0 04:10 pts/25   00:00:00 grep --color=auto mininet
```

### 为路由器r1的网络命名空间创建软连接
```Bash
sudo ln -s /proc/19320/ns/net /var/run/netns/r1_ns
```
注：需要保证/var/run/netns/的存在


### 创建Veth pair，并分别添加到R1和br0命名空间
```Bash
sudo ip link add veth0 type veth peer name veth1
sudo ip link set veth0 master br0
sudo ip link set veth1 netns r1_ns
```
### 配置地址，并启动
```Bash
sudo ip netns exec r1_ns ip addr add 10.1.1.2/24 dev veth1
sudo ip addr add 10.1.1.1/24 dev br0
sudo ip link set br0 up
sudo ip link set veth0 up
sudo ip netns exec r1_ns ip link set veth1 up
```
至此网络已经是互通的了，其余路由器的配置相同，接着这两个命名空间下分别运行gRpc服务端和客户端，完成控制功能。

## 部署控制器

我们使用gRpc来完成控制器和路由器之间的通信，为此需要完成gRpc Server和gRpc Client，其中Server在路由器中运行，Client作为控制器部署。

### Proto

定义三个rpc命令，分别是获取一个设备指定网卡的网络信息、获得一个设备全部网卡的网络信息以及发送命令。
```Bash
service IfaceInfo {
    rpc GetOneInfo(OneDevice) returns (Address) {}
    rpc GetAllInfo(ServalDevice) returns (stream Address) {}
    rpc SendCmd(Command) returns (Response) {} 
}
```
详情见ifaceinfo.proto

执行
```Bash
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. ifaceinfo.proto
```
生成ifaceinfo_pb2_grpc.py与ifaceinfo_pb2.py，供gRpc Server和Client使用

### gRpc Server

实现的主要功能就是Proto定义的三个rpc命令，详情见ifaceinfo_grpc_server.py，运行的时候指定节点的名字和地址，如针对R1路由器，
```Bash
python ifaceinfo_grpc_server.py --node r1 --address 10.1.1.2:50051
```
路由器名字与地址的映射关系如下：

```Python
routers = {
    'r1': '10.1.1.2:50051',   
    'r2': '10.1.1.3:50051',   
    'r3': '10.1.1.4:50051',
    'r4': '10.1.1.5:50051'
}
```
### gRpc Client

gRpc Client 作为控制器实现，其实现的功能包括，获得全网的拓扑，包括主机和路由器，以及全部的链路；计算主机之间的最短路径，即首先获得主机所连接的路由器，计算路由器之间的最短路径；下放路由命令；详情见ifaceinfo_grpc_client.py

运行

```Bash

python ifaceinfo_grpc_client.py

```

即可观察到，转发命令通过控制器向路由器下发，主机之间可以通信

## 注意

还是要提前禁止反向路径检测机制！！！





