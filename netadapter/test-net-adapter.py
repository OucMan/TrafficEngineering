# coding:utf-8

import netifaces
import json
import argparse


def get_interfaces(router):
    res = []
    all_interfaces = netifaces.interfaces()
    for inf in all_interfaces:
        if router in inf:
            res.append(inf)
    return res


def get_adapter_info(interfaces):
    res = []
    for inface in interfaces:
        iface_info = {}
        iface_info['name'] = inface
        iface_info['addresses'] = {}

        ipv6_addr = netifaces.ifaddresses(inface)[netifaces.AF_INET6][0]['addr'].split('%')[0]
        iface_info['addresses']['ipv6'] = ipv6_addr

        ipv6_mask = netifaces.ifaddresses(inface)[netifaces.AF_INET6][0]['netmask']
        iface_info['addresses']['mask'] = ipv6_mask

        mac_addr = netifaces.ifaddresses(inface)[netifaces.AF_PACKET][0]['addr']
        iface_info['addresses']['mac'] = mac_addr

        res.append(iface_info)
    return res


# python xxx.py --node r1
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--node", type=str, required=True, help="device name")

    # obtain the router name
    router_name = parser.parse_args().node

    # obtain the data interfaces
    interfaces = get_interfaces(router_name)

    # obtain the interfaces' address information
    iface_info = get_adapter_info(interfaces)

    info_json = json.dumps(iface_info)

    print(info_json)
