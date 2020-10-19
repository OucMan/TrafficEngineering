# TrafficEngineering

SDN Architecture: build a sdn controller to obtain the underlayer network topology, compute the option forwarding path, and send routing instructions to the SR switches.

SRv6: use SRv6 device by linux kernel

gRPC：connection between SRv6 Router and sdn controller is on gRPC

P.S.

There has two types network, i.e., data network and control network. The data network is ipv6 network to transmit business packets, and the control network is to connect the controller and routers. Specifically, we use veth pair to achieve the communication between controller and router in different network namespace (see control-network/control_network.md for specific commands).


