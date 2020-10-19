1、查看路由器的网络命名空间

# 查看进程号
ps -ef | grep mininet

root       2562   2557  0 00:57 pts/2    00:00:00 bash --norc -is mininet:a
root       2564   2557  0 00:57 pts/6    00:00:00 bash --norc -is mininet:b
root       2566   2557  0 00:57 pts/11   00:00:00 bash --norc -is mininet:c
root       2568   2557  0 00:57 pts/20   00:00:00 bash --norc -is mininet:r1
root       2570   2557  0 00:57 pts/21   00:00:00 bash --norc -is mininet:r2
root       2572   2557  0 00:57 pts/22   00:00:00 bash --norc -is mininet:r3
root       2574   2557  0 00:57 pts/23   00:00:00 bash --norc -is mininet:r4
xujianf+   2842   2807  0 00:58 pts/24   00:00:00 grep --color=auto mininet

例如，路由器r1的进程号为2568

# 查看路由器r1所在的网络命名空间
sudo ls -al /proc/2568/ns
total 0
dr-x--x--x 2 root root 0 Oct 19 00:57 .
dr-xr-xr-x 9 root root 0 Oct 19 00:57 ..
lrwxrwxrwx 1 root root 0 Oct 19 01:00 cgroup -> cgroup:[4026531835]
lrwxrwxrwx 1 root root 0 Oct 19 01:00 ipc -> ipc:[4026531839]
lrwxrwxrwx 1 root root 0 Oct 19 00:57 mnt -> mnt:[4026532834]
lrwxrwxrwx 1 root root 0 Oct 19 00:57 net -> net:[4026532836]
lrwxrwxrwx 1 root root 0 Oct 19 01:00 pid -> pid:[4026531836]
lrwxrwxrwx 1 root root 0 Oct 19 01:00 pid_for_children -> pid:[4026531836]
lrwxrwxrwx 1 root root 0 Oct 19 01:00 user -> user:[4026531837]
lrwxrwxrwx 1 root root 0 Oct 19 01:00 uts -> uts:[4026531838]

查看其它的设备，可以发现设备的网络命名空间不同，这也证明了mininet通过namespace来实现网络隔离

注：在root空间下利用ip netns list不能看到mininet创建的网络命名空间，因为mininet创建的网络命名空间为nameless，而ip netns list只能查看有名字的网络命名空间，比如通过ip netns add命令创建的网络命名空间

# 为路由器r1的网络命名创建软连接，便于后续操作

sudo ln -s /proc/2568/ns/net /var/run/netns/r1_ns

2、创建网桥
sudo ip link add name br0 type bridge

3、创建veth-pair
sudo ip link add veth0 type veth peer name veth1

4、为不同的网络空间添加端口

# 向root空间中的网桥中添加端口
sudo ip link set veth0 master br0

# 向路由器r1网络命名空间中添加端口
sudo ip link set veth1 netns r1_ns

5、配置地址
sudo ip netns exec r1_ns ip addr add 10.1.1.2/24 dev veth1
sudo ip addr add 10.1.1.1/24 dev br0

6、启动设备
sudo ip link set br0 up
sudo ip link set veth0 up
sudo ip netns exec r1_ns ip link set veth1 up

至此网络已经是互通的了，在两个命名空间下运行grpc服务端和客户端，运行正常







