# coding: utf-8

__author__ = 'xujianfeng@iie.ac.cn'
__version__ = '0.0.1'

from raft.node import Node
import sys
sys.path.append('..')


if __name__ == '__main__':
    conf = {
        'id': 'node_3',
        'addr': ('localhost', 10003),
        'peers': {
            'node_1': ('localhost', 10001),
            'node_2': ('localhost', 10002)
        }
    }
    node = Node(conf)
    node.run()

