import sys
import socket

if len(sys.argv) < 4:
    print('Input: IP address, port and message for sending')
    sys.exit(1)

with socket.socket() as client_socket:
    ip, port, message = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    client_socket.connect((ip, port))
    client_socket.send(message.encode())
    response = client_socket.recv(1024)
    print(response.decode())
