# 启动拓扑

## sudo python Topo.py

Topo.py代码主要执行的动作有：创建4个路由器与3个主机，并设置静态路由；创建设备之间的链路；对于路由器来说，增加loopback接口，并将其设置为SR中的设备segment，同时设置所有的接口支持SRv6。
