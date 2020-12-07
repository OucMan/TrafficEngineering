# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ifaceinfo_v2_pb2 as ifaceinfo__v2__pb2


class IfaceInfoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOneInfo = channel.unary_unary(
                '/IfaceInfo/GetOneInfo',
                request_serializer=ifaceinfo__v2__pb2.OneDevice.SerializeToString,
                response_deserializer=ifaceinfo__v2__pb2.Address.FromString,
                )
        self.GetAllInfo = channel.unary_stream(
                '/IfaceInfo/GetAllInfo',
                request_serializer=ifaceinfo__v2__pb2.ServalDevice.SerializeToString,
                response_deserializer=ifaceinfo__v2__pb2.Address.FromString,
                )
        self.SendCmd = channel.unary_unary(
                '/IfaceInfo/SendCmd',
                request_serializer=ifaceinfo__v2__pb2.Command.SerializeToString,
                response_deserializer=ifaceinfo__v2__pb2.Response.FromString,
                )
        self.GetTask = channel.unary_stream(
                '/IfaceInfo/GetTask',
                request_serializer=ifaceinfo__v2__pb2.Empty.SerializeToString,
                response_deserializer=ifaceinfo__v2__pb2.PacketIn.FromString,
                )


class IfaceInfoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetOneInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendCmd(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IfaceInfoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOneInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOneInfo,
                    request_deserializer=ifaceinfo__v2__pb2.OneDevice.FromString,
                    response_serializer=ifaceinfo__v2__pb2.Address.SerializeToString,
            ),
            'GetAllInfo': grpc.unary_stream_rpc_method_handler(
                    servicer.GetAllInfo,
                    request_deserializer=ifaceinfo__v2__pb2.ServalDevice.FromString,
                    response_serializer=ifaceinfo__v2__pb2.Address.SerializeToString,
            ),
            'SendCmd': grpc.unary_unary_rpc_method_handler(
                    servicer.SendCmd,
                    request_deserializer=ifaceinfo__v2__pb2.Command.FromString,
                    response_serializer=ifaceinfo__v2__pb2.Response.SerializeToString,
            ),
            'GetTask': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTask,
                    request_deserializer=ifaceinfo__v2__pb2.Empty.FromString,
                    response_serializer=ifaceinfo__v2__pb2.PacketIn.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'IfaceInfo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IfaceInfo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetOneInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IfaceInfo/GetOneInfo',
            ifaceinfo__v2__pb2.OneDevice.SerializeToString,
            ifaceinfo__v2__pb2.Address.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/IfaceInfo/GetAllInfo',
            ifaceinfo__v2__pb2.ServalDevice.SerializeToString,
            ifaceinfo__v2__pb2.Address.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendCmd(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/IfaceInfo/SendCmd',
            ifaceinfo__v2__pb2.Command.SerializeToString,
            ifaceinfo__v2__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/IfaceInfo/GetTask',
            ifaceinfo__v2__pb2.Empty.SerializeToString,
            ifaceinfo__v2__pb2.PacketIn.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
