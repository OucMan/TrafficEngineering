# 有控制器模式（主动式路由下发）

在版本０基础上，增加控制器，控制器实现的功能如下：获取实时网络拓扑，利用最短路径算法得到转发路径，主动下发路由规则到路由器。

## 拓扑

数据面拓扑和版本0一致，控制通路使用veth pair来实现，完整拓扑见Topo.png。

路由器与控制器之间的Veth Pair设置如下

Br-R1: Veth0(10.1.1.1/24)<->Veth1(10.1.1.2/24)
Br-R2: Veth2(10.1.1.3/24)<->Veth3(10.1.1.4/24)
Br-R3: Veth4(10.1.1.5/24)<->Veth5(10.1.1.6/24)
Br-R4: Veth6(10.1.1.7/24)<->Veth7(10.1.1.8/24)

控制器与路由器之间的通信使用gRpc机制

## 创建控制通路

以R1为例，创建R1与控制器之间的控制通道，其余通道同理

### Root命名空间创建br0网桥（创建一次就好）

sudo ip link add name br0 type bridge


### 查看R1进程号

ps -ef | grep mininet
root      19314  19309  0 04:10 pts/11   00:00:00 bash --norc -is mininet:a
root      19316  19309  0 04:10 pts/12   00:00:00 bash --norc -is mininet:b
root      19318  19309  0 04:10 pts/20   00:00:00 bash --norc -is mininet:c
root      19320  19309  0 04:10 pts/21   00:00:00 bash --norc -is mininet:r1
root      19322  19309  0 04:10 pts/22   00:00:00 bash --norc -is mininet:r2
root      19324  19309  0 04:10 pts/23   00:00:00 bash --norc -is mininet:r3
root      19326  19309  0 04:10 pts/24   00:00:00 bash --norc -is mininet:r4
xujianf+  19572  19559  0 04:10 pts/25   00:00:00 grep --color=auto mininet


### 为路由器r1的网络命名空间创建软连接

sudo ln -s /proc/19320/ns/net /var/run/netns/r1_ns

注：需要保证/var/run/netns/的存在


### 创建Veth pair，并分别添加到R1和br0命名空间

sudo ip link add veth0 type veth peer name veth1

sudo ip link set veth0 master br0

sudo ip link set veth1 netns r1_ns

### 配置地址，并启动

sudo ip netns exec r1_ns ip addr add 10.1.1.2/24 dev veth1

sudo ip addr add 10.1.1.1/24 dev br0

sudo ip link set br0 up

sudo ip link set veth0 up

sudo ip netns exec r1_ns ip link set veth1 up

至此网络已经是互通的了，其余路由器的配置相同，接着这两个命名空间下分别运行gRpc服务端和客户端，完成控制功能。

## 部署控制器




