import grpc
import test_pb2
import test_pb2_grpc


def run():
    with grpc.insecure_channel('0.0.0.0:50052') as channel:
        stub = test_pb2_grpc.SquareRootServiceStub(channel)
        response = stub.squareRoot(test_pb2.Number(input=7))
        print(response.resulta)

if __name__ == '__main__':
    run()