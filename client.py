import grpc
import greet_pb2
import greet_pb2_grpc

CONNECTION_STRING = "localhost:12345"

def run():
    with grpc.insecure_channel(CONNECTION_STRING) as channel: # channel allows to make grpc calls
        stub = greet_pb2_grpc.GreeterStub(channel)

        input_name = input("What's your name?\n")

        request = greet_pb2.GreetRequest(name = input_name)
        greeting_message = stub.Greet(request)

        print("Received: " + greeting_message.greeting_message)

if __name__ == "__main__":
    run()