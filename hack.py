import sys
import socket
from itertools import product
from string import ascii_lowercase, digits


def pass_gen():
    for i in range(1, 11):
        for combination in product(ascii_lowercase + digits, repeat=i):
            yield ''.join(combination)


if len(sys.argv) < 3:
    print('Input: IP address and port for sending')
    sys.exit(1)
ip, port = sys.argv[1], int(sys.argv[2])

gen = pass_gen()
with socket.socket() as client_socket:
    client_socket.connect((ip, port))
    while True:
        message = next(gen)
        client_socket.send(message.encode())
        response = client_socket.recv(256).decode()
        if response == 'Connection success!':
            client_socket.close()
            break
print(message)
