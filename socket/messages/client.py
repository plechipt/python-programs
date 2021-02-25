import os
import sys
import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 80

cmd_mode = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    server_message = s.recv(1024).decode('utf-8')
    print(server_message)

    if server_message == 'exit -f':
        sys.exit()

    elif server_message == 'cmdon':
        cmd_mode = True
    
    elif server_message == 'cmdoff':
        cmd_mode = False

    #####

    # Warning! Do not abuse this! This is meant to be only for fun!
    '''
    # Enter command to client
    if cmd_mode and server_message != 'cmdon':
        os.popen(server_message)
    '''

    client_input = input('\nclient: ')

    if client_input == '':
        client_input = 'Client has nothing entered!'

    # Send message to server
    s.send(client_input.encode('utf-8'))
