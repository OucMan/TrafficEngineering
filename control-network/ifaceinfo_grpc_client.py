# coding:utf-8
import grpc
import ifaceinfo_pb2
import ifaceinfo_pb2_grpc


def run():
    channel = grpc.insecure_channel('10.1.1.2:50051')
    stub = ifaceinfo_pb2_grpc.IfaceInfoStub(channel)
    print('---------------GetOneInfo----------------')
    response = stub.GetOneInfo(ifaceinfo_pb2.OneDevice(name='r1-eth0'))
    print(response)
    response = stub.GetOneInfo(ifaceinfo_pb2.OneDevice(name='r1-eth1'))
    print(response)
    print('---------------GetAllInfo----------------')
    response = stub.GetAllInfo(ifaceinfo_pb2.ServalDevice(name='all'))
    for address in response:
        print(address)


if __name__ == '__main__':
    run()
