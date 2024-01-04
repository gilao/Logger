import logging
import os
import time

import grpc
from concurrent import futures
from pkg.proto import log_pb2
from pkg.proto import log_pb2_grpc
from pkg.logger.logger import log

num = 0
def a():
    p = 'text'
    while True:
        log.debug('time ' + p)
        # log.info('info ' + p)
        # log.error('error ' + p)
        # log.warning('warning ' + p)
        # log.critical('critical ' + p)
        # now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        # file_path = 'file.log'
        # file_descriptor = os.open(file_path, os.O_RDWR | os.O_CREAT)
        # os.write(file_descriptor, b"Hello, world!")
        # os.close(file_descriptor)
        # os.rename(file_path,f"{now}.{file_path}")
        time.sleep(1)
class LogModel(log_pb2_grpc.LogModelServicer):
    def logging(self, request, context):
        global num
        num = num + 1
        result = str(num)
        response = log_pb2.Response()
        response.result = result
        # log.debug(request.query)
        log.info(request.query)
        # log.error(request.query)
        # log.warning(request.query)
        # log.critical(request.query)
        return response
# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # server = grpc.server(futures.ThreadPoolExecutor(max_workers=201))
    # log_pb2_grpc.add_LogModelServicer_to_server(LogModel(), server)
    # server.add_insecure_port("[::]:50052")
    # server.start()
    # print("Server started on port 50052")
    # server.wait_for_termination()
    a()


