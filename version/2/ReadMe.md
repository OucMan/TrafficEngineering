# 有控制器模式（响应式安装规则）

数据包到达入口路由器，发现无转发规则与其匹配，便将转发请求上传至控制器，控制器根据获得的全局拓扑计算得到转发路径，并将路由下发至路由器


## Packet-In实现

我们使用TUN设备+默认路由的方式实现路由器主动将未能匹配路由规则的数据包信息上报给控制器。

### TUN设备

创建一个TUN设备叫做packet_in

```Python
def create_tun(tun_name):
    tun = TunTapDevice(name=tun_name, flags=(IFF_TUN | IFF_NO_PI))
    tun.addr = '10.6.0.1'
    tun.dstaddr = '0.0.0.0'
    tun.netmask = '0.0.0.0'
    tun.mtu = 1500
    return tun
```

### 默认路由

创建完TUN设备后，安装默认路由，将不能与路由表匹配的数据包信息发送给控制器
```Python
def default_route(tun):
    return os.system('route add default gw ' + tun.addr + ' ' + tun.name)
```
本质上就是执行Linux命令
```Bash
route add default via 10.6.0.1 dev packet_in
```

### gRpc服务器主动向客户端发送信息

gRpc提供的通信机制中，无法实现服务端主动向客户端发送信息，因此我们使用客户端向服务端发送“空信息”来向服务端请求信息。具体流程如下，我们在每一个路由器中声明一个具有一定大小的buffer，用来存储无法匹配路由表的数据包信息，每一段时间控制器来主动请求这个消息，因为请求消息是空，因此看起来像路由器主动向控制器发送消息，通过这种方式来实现“伪主动”。

### 代码介绍

ifaceinfo_v2_grpc_server.py：运行在路由器一侧，除了具备版本一的全部功能，还包括创建TUN设备，创建默认路由，保存并向控制器反馈“table-miss”数据包信息，即未与路由表匹配的数据包信息。

ifaceinfo_v2_grpc_client.py：控制器，除了具备版本一的全部功能，还包括接收Packet-In信息的功能，进而根据此信息得到源于目的主机，以及其中间的转发设备，创建路由规则并下发。

send.py：发包程序，用来测试packet_in机制，由主机A执行，注意，其中的目的MAC地址设置为R1中与A相连端口的MAC地址。

send2.py：发包程序，用来测试packet_in机制，由主机B执行，注意，其中的目的MAC地址设置为R4中与B相连端口的MAC地址。

对于ifaceinfo_v2.proto文件，增加了一个RPC功能以及两种消息类型
```Bash
rpc GetTask (Empty) returns (stream PacketIn);

message PacketIn {
    string device = 1;
    string src = 2;
    string dst = 3;
}

message Empty {
}

```
    

