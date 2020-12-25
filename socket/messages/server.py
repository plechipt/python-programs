import socket
from win10toast import ToastNotifier

HOST = '192.168.1.167'
PORT = 9090
toaster = ToastNotifier()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()
client, address = server.accept()

toaster.show_toast(f'Client is connected!', 'hahahah')

while True:
    server_input = input('\n...: ')

    if server_input == '':
        continue

    client.send(server_input.encode('utf-8'))
    client_message = client.recv(1024).decode('utf-8')

    print(client_message)