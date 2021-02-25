import sys
import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 80

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

print('Waiting for client...')

server.listen()
client, address = server.accept()

while True:
    server_input = input('\nserver: ')

    if server_input == '':
        continue

    client.send(server_input.encode('utf-8'))

    if server_input == 'exit -f':
        sys.exit()
        
    client_message = client.recv(1024).decode('utf-8')
    print(client_message)