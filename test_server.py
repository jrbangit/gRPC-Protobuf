import grpc
import test_pb2
import test_pb2_grpc
from concurrent import futures

class SquareRootServiceServicer(test_pb2_grpc.SquareRootServiceServicer):
    def squareRoot(self, request, context):
        resulta = request.input * request.input
        return test_pb2.Result(resulta = resulta)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    test_pb2_grpc.add_SquareRootServiceServicer_to_server(SquareRootServiceServicer(), server)
    print("Server Started!")
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

main()
