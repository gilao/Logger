# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pkg.proto import log_pb2 as pkg_dot_proto_dot_log__pb2


class LogModelStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.logging = channel.unary_unary(
                '/proto.LogModel/logging',
                request_serializer=pkg_dot_proto_dot_log__pb2.Request.SerializeToString,
                response_deserializer=pkg_dot_proto_dot_log__pb2.Response.FromString,
                )


class LogModelServicer(object):
    """Missing associated documentation comment in .proto file."""

    def logging(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LogModelServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'logging': grpc.unary_unary_rpc_method_handler(
                    servicer.logging,
                    request_deserializer=pkg_dot_proto_dot_log__pb2.Request.FromString,
                    response_serializer=pkg_dot_proto_dot_log__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.LogModel', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LogModel(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def logging(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.LogModel/logging',
            pkg_dot_proto_dot_log__pb2.Request.SerializeToString,
            pkg_dot_proto_dot_log__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
