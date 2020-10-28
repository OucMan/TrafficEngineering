# coding:utf-8
import grpc
import ifaceinfo_pb2
import ifaceinfo_pb2_grpc
import IPy

routers = {
    'r1': '10.1.1.2:50051',
    'r2': '10.1.1.3:50051',
    'r3': '10.1.1.4:50051',
    'r4': '10.1.1.5:50051'
}


class Controller(object):

    def __init__(self):
        self.channels = {}

    def topo_discover(self):
        self.update_channel()
        device_info = self.get_all_device_info(self.channels)
        nodes, edges = self.build_topology(device_info)

    def update_channel(self):
        self.channels = {}
        for name, address in routers.items():
            channel = grpc.insecure_channel(address)
            if channel:
                self.channels[name] = channel

    def get_all_device_info(self, channels):
        if not channels:
            return None
        res = {}
        for n, ch in channels.items():
            stub = ifaceinfo_pb2_grpc.IfaceInfoStub(ch)
            resp = stub.GetAllInfo(ifaceinfo_pb2.ServalDevice(name='all'))
            res[n] = []
            for r in resp:
                tmp = {}
                ipv6 = IPy.IP(r.ipv6).strBin()
                mask = int(r.mask.split('/')[1])
                network = ipv6[:mask]
                tmp[r.iface_name] = [r.ipv6, network]
                res[n].append(tmp)
        return res

    def build_topology(self, devices):
        if not devices:
            return None, None
        nodes = devices.keys()
        edges = []
        for n in nodes:
            for m in nodes:
                if n == m:
                    continue
                edge = self.get_link(n, m, devices)
                if edge:
                    edges.append(edge)
        return nodes, edges

    def get_link(self, start, end, devices):
        start_ports = devices[start]
        end_ports = devices[end]
        for sp in start_ports:
            sp_name = sp.keys()[0]
            sp_addr = sp[sp_name][0]
            if sp_addr.startswith('fe80'):
                continue
            sp_net = sp[sp_name][1]
            for ep in end_ports:
                ep_name = ep.keys()[0]
                ep_addr = ep[ep_name][0]
                if ep_addr.startswith('fe80'):
                    continue
                ep_net = ep[ep_name][1]
                if sp_net == ep_net:
                    return {(start, end): (sp_name, ep_name)}
        return None


if __name__ == '__main__':
    c = Controller()
    c.topo_discover()

'''

{

'r4': [
	{u'r4-eth1': 
		[u'2001:14::2', u'ffff:ffff:ffff:ffff::/64']
	}, 
	{u'r4-eth0': 
		[u'2001:24::2', u'ffff:ffff:ffff:ffff::/64']
	}, 
	{u'r4-eth2': 
		[u'2001:34::2', u'ffff:ffff:ffff:ffff::/64']
	}, 
	{u'r4-eth3': 
		[u'fe80::f0dd:32ff:fe71:334e', u'ffff:ffff:ffff:ffff::/64']
	}, 
	{u'r4-eth4': 
		[u'2001:4b::1', u'ffff:ffff:ffff:ffff::/64']
	}], 
'r1': 
	[{u'r1-eth2':
		[u'fe80::d83f:80ff:fe55:3d43', u'ffff:ffff:ffff:ffff::/64']
	}, 
	{u'r1-eth3':
		[u'2001:1a::1', u'ffff:ffff:ffff:ffff::/64']
	}, 
	{u'r1-eth0': 
		[u'2001:12::1', u'ffff:ffff:ffff:ffff::/64']
	}, 
	{u'r1-eth1': 
		[u'2001:14::1', u'ffff:ffff:ffff:ffff::/64']
	}], 
'r2':
	 [{u'r2-eth0': 
	 	[u'2001:12::2', u'ffff:ffff:ffff:ffff::/64']
	 }, 
	 {u'r2-eth1': 
	 	[u'2001:23::1', u'ffff:ffff:ffff:ffff::/64']
	 }, 
	 {u'r2-eth2': 
	 	[u'2001:24::1', u'ffff:ffff:ffff:ffff::/64']
	 }], 
'r3': 
	[{u'r3-eth0': 
		[u'2001:23::2', u'ffff:ffff:ffff:ffff::/64']
	}, 
	{u'r3-eth2': 
		[u'fe80::744f:edff:fe77:7617', u'ffff:ffff:ffff:ffff::/64']
	}, 
	{u'r3-eth3': 
		[u'2001:3c::1', u'ffff:ffff:ffff:ffff::/64']
	}, 
	{u'r3-eth1': 
		[u'2001:34::1', u'ffff:ffff:ffff:ffff::/64']}]
}

'''
