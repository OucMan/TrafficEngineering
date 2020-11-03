from concurrent import futures
import time
import random
import grpc
import contact_pb2
import contact_pb2_grpc

class Server(contact_pb2_grpc.ContactServicer):

    def __init__(self):
        self.buffers = []

    def sendStatus(self, request_iterator, context):
        for note in request_iterator:
            yield contact_pb2.Result(ret=f'服务端接收到消息:{note.msg}')

    def getTask(self, request, context):
        print('服务端已接受到客户端上线通知，开始发送任务到客户端\n')
        while self.buffers:
            yield self.buffers.pop(0)

    def addTask(self):
        if len(self.buffers) > 100:
            return
        num = random.randint(100, 200)
        self.buffers.append(contact_pb2.ServerMsg(task=f'任务:{num}'))

    def tellResult(self, request_iterator, context):
        for response in request_iterator:
            print(f'我已经知道客户端接收到我发过去的任务:{response.ret}')
        return contact_pb2.Empty()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    s = Server()
    contact_pb2_grpc.add_ContactServicer_to_server(s, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            i = random.randint(1, 5)
            if i > 3:
                s.addTask()
            time.sleep(i)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()

