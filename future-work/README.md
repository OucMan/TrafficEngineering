# 未来工作

上述工作中，控制器采用的是单例控制器，而为了增加控制平面的可扩展性以及高可用性，控制平面往往使用集群的方式实现，因此未来将要实现控制器集群。

# Raft协议

分布式集群中，保证各个节点间的数据一致性是关键所在，而Raft协议便是保持集群数据强一致性的算法之一。由于其简单易懂，拟采取该协议作为控制器之间的一致性协议。

Raft官网：https://raft.github.io/

本部分首先对Raft协议以及其Python实现做简单介绍，后续工作为将控制器逻辑与Raft协议进行整合。

# 参考

Raft简介：https://www.jianshu.com/p/8e4bbe7e276c

Raft的Python实现：https://github.com/hangsz/raft

