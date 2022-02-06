
def receive_command():
    import time
    import socket
    import sys
    import os

    s = socket.socket()
    host = '192.168.1.5'
    # host = 'GAMING-PC'
    port = 9999

    try:
        s.connect((host, port))
        print("Connected to server")
        
        command = s.recv(1024).decode()
        print(f"Command Received : '{command}' ...")

        if command == 'shutdown':
            print("Shutting down...")
            os.system('shutdown -s -t 0')
                
    except:
        print("Error connecting to server..retrying")
while True:
    receive_command()
'''

import socket

c= socket.socket()
c.connect(('192.168.1.5',9999))
print("Connected to server")
print(c.recv(1024))

'''
