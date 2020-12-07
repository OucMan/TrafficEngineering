# coding:utf-8
import grpc
import ifaceinfo_v2_pb2
import ifaceinfo_v2_pb2_grpc
import IPy
import networkx as nx
import matplotlib.pyplot as plt
import time


routers = {
    'r1': '10.1.1.2:50051',
    'r2': '10.1.1.3:50051',
    'r3': '10.1.1.4:50051',
    'r4': '10.1.1.5:50051'
}

hosts = {
    'a': ['10.0.0.1', 24],
    'b': ['10.0.2.1', 24],
    'c': ['10.0.1.1', 24]
}


class Controller(object):

    def __init__(self):
        self.channels = {}
        self.stubs = {}
        self.graph = None
        self.nodes = []
        self.edges = []
        self.access_ports = {}
        self.interior_ports = {}
        self.shortest_paths = {}

    def topo_discover(self):
        self.update_channel()
        device_info = self.get_all_device_info(self.channels)  # {router_name : {port_name : [ip, mask]}}
        self.nodes, self.edges = self.build_topology(device_info)  # [router_name], {(src_host. dst_host): (src_port, dst_port)}
        self.graph = self.create_graph(self.nodes, self.edges)
        self.shortest_paths = self.get_shortest_paths(self.graph)

        # print(self.ping_between_two_hosts(hosts['a'], hosts['c']))

        # print(self.get_path_between_two_routers('r1', 'r2'))

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
        self.stubs = {}
        for n, ch in channels.items():
            stub = ifaceinfo_v2_pb2_grpc.IfaceInfoStub(ch)
            self.stubs[n] = stub
            resp = stub.GetAllInfo(ifaceinfo_v2_pb2.ServalDevice(name='all'))
            res[n] = {}
            for r in resp:
                ipv6 = IPy.IP(r.ipv6).strBin()
                if '/' in r.mask:
                    mask = int(r.mask.split('/')[1])
                else:
                    mask = IPy.IP(r.mask).strBin().count('1')
                network = ipv6[:mask]
                res[n][r.iface_name] = [r.ipv6, network]
        return res

    def build_topology(self, devices):
        if not devices:
            return None, None
        self.access_ports = {}
        self.interior_ports = {}
        nodes = devices.keys()
        edges = {}
        for n in nodes:
            for m in nodes:
                if n == m:
                    continue
                node_pair, port_pair = self.get_link(n, m, devices)
                if node_pair and port_pair:
                    self.interior_ports.setdefault(node_pair[0], {})
                    self.interior_ports.setdefault(node_pair[1], {})
                    edges[node_pair] = port_pair
                    tmp_start = devices[node_pair[0]][port_pair[0]]
                    tmp_end = devices[node_pair[1]][port_pair[1]]
                    self.interior_ports[node_pair[0]][port_pair[0]] = tmp_start
                    self.interior_ports[node_pair[1]][port_pair[1]] = tmp_end

        for d in devices:
            self.access_ports.setdefault(d, {})
            for p in devices[d].keys():
                if p not in self.interior_ports[d]:
                    self.access_ports[d][p] = devices[d][p]

        return nodes, edges

    def get_link(self, start, end, devices):
        start_ports = devices[start]
        end_ports = devices[end]
        for sp_name in start_ports.keys():
            sp_addr = start_ports[sp_name][0]
            sp_net = start_ports[sp_name][1]
            for ep_name in end_ports.keys():
                ep_addr = end_ports[ep_name][0]
                ep_net = end_ports[ep_name][1]
                if sp_net == ep_net:
                    return (start, end), (sp_name, ep_name)
        return None, None

    def create_graph(self, nodes, edges):
        G = nx.DiGraph()
        G.add_nodes_from(nodes)
        G.add_edges_from(edges.keys(), weight=1)
        return G

    def display_graph(self, graph):
        nx.draw(graph, with_labels=True)
        plt.show()

    def get_shortest_paths(self, graph):
        return dict(nx.all_pairs_dijkstra_path(graph))

    def get_path_between_two_routers(self, start, end):
        path = None
        if start in self.shortest_paths.keys():
            if end in self.shortest_paths[start].keys():
                path = self.shortest_paths[start][end]
        if not path or len(path) == 1:
            return []
        res = []
        for i in range(len(path) - 1):
            src = path[i]
            dst = path[i + 1]
            if (src, dst) not in self.edges.keys():
                return []
            res.append((src, self.edges[(src, dst)][0]))
        return res

    def ping_between_two_hosts(self, src, dst):
        src_net = IPy.IP(src[0]).strBin()[:src[1]]
        dst_net = IPy.IP(dst[0]).strBin()[:dst[1]]
        src_router = None
        dst_router = None
        src_router_port = None
        dst_router_port = None
        for r in self.access_ports.keys():
            for p in self.access_ports[r].keys():
                if self.access_ports[r][p][1] == src_net:
                    src_router = r
                    src_router_port = p
                if self.access_ports[r][p][1] == dst_net:
                    dst_router = r
                    dst_router_port = p
        if not src_router or not src_router_port or not dst_router or not dst_router_port:
            return None
        res = self.get_path_between_two_routers(src_router, dst_router)
        res.append((dst_router, dst_router_port))
        return res

    def send_route(self, route, cmd):
        stub = self.stubs[route]
        resp = stub.SendCmd(ifaceinfo_v2_pb2.Command(cmd=cmd))
        print(resp)

    def get_task(self, stub):
        try:
            for task in stub.GetTask(ifaceinfo_v2_pb2.Empty()):
                print('Packet-in:  ' + task.device + '  ' + task.src + '  ' + task.dst)
                print('Obtain the forwarding path according to the above functions and issue the corresponding forwarding rules...')
        except Exception as e:
            print(e)
            return

    def run(self):
        self.topo_discover()
        print(self.stubs)

        while True:
            try:
                self.get_task(self.stubs['r1'])
                self.get_task(self.stubs['r2'])
                self.get_task(self.stubs['r3'])
                self.get_task(self.stubs['r4'])
                time.sleep(3)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    c = Controller()
    c.run()
