# coding: utf-8

__author__ = 'xujianfeng@iie.ac.cn'
__version__ = '0.0.1'

from raft.node import Node
import sys
sys.path.append('..')


if __name__ == '__main__':
    conf = {
        'id': 'node_1',
        'addr': ('localhost', 10001),
        'peers': {
            'node_2': ('localhost', 10002),
            'node_3': ('localhost', 10003)
        }
    }
    node = Node(conf)
    node.run()

