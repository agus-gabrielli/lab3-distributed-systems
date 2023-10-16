from concurrent import futures
import grpc
import greet_pb2
import greet_pb2_grpc

PORT = "12345"
MAX_THREADS = 5


class Greeter(greet_pb2_grpc.GreeterServicer):
    def Greet(self, request, context):
        print(f"Greet request made:\n {request}")

        message = f"Ciao {request.name}! Spero che stia bene"

        return greet_pb2.GreetReply(greeting_message = message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_THREADS))
    greet_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("localhost:" + PORT)
    server.start()

    print("Server started, listening on port " + PORT)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()