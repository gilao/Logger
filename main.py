import logging
import os
import time

import grpc
from concurrent import futures
from pkg.proto import log_pb2
from pkg.proto import log_pb2_grpc
from pkg.logger import logger

num = 0
my_logger = logger.Logger('test.log',1)
def a():
    p = 'text'
    while True:
        my_logger.debug('debug ' + p)
        # my_logger.info('info ' + p)
        # my_logger.error('error ' + p)
        # my_logger.warning('warning ' + p)
        # my_logger.critical('critical ' + p)
        # now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        # file_path = 'file.log'
        # file_descriptor = os.open(file_path, os.O_RDWR | os.O_CREAT)
        # os.write(file_descriptor, b"Hello, world!")
        # os.close(file_descriptor)
        # os.rename(file_path,f"{now}.{file_path}")
        # time.sleep(0.5)
        my_logger.debug('debug 111')
class LogModel(log_pb2_grpc.LogModelServicer):
    def logging(self, request, context):
        global num
        num = num + 1
        result = str(num)
        response = log_pb2.Response()
        response.result = result
        # my_logger.debug(request.query)
        my_logger.info(request.query)
        # my_logger.error(request.query)
        # my_logger.warning(request.query)
        # my_logger.critical(request.query)
        return response
# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
    log_pb2_grpc.add_LogModelServicer_to_server(LogModel(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    print("Server started on port 50052")
    server.wait_for_termination()
    # a()


