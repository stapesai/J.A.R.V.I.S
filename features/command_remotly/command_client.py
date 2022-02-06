def receive_command():
    import time
    import socket
    import sys
    import os

    s = socket.socket()
    host = '169.254.20.74'
    # host = 'GAMING-PC'
    port = 80
    try:
        s.connect((host, port))
        print("Connected to server")
        
        command = s.recv(1024).decode()
        print("Received command: " + command)
        if command == 'shutdown':
            print("Shutting down...")
            # os.system('shutdown -s -t 0')
            # break
        else:
            print(f"Command Received : '{command}' ...")
                
    except:
        print("Error connecting to server..retrying")
while True:
    receive_command()