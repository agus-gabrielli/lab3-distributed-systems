# lab3-distributed-systems

Command to generate python code compiling the proto file
python3 -m grpc_tools.protoc -I protos --python_out=. --pyi_out=. --grpc_python_out=. protos/greet.proto