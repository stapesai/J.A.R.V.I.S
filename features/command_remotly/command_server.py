def send_command(command):
    import time
    import socket
    import sys
    import os

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # s.timeout(0.1)
    host = socket.gethostname()
    print("Host: " + host)
    port = 80
    command = input("Enter command: ")

    try:
        s.bind((host, port))
        print("Listening for connections...")
        s.listen(5)
        conn, addr = s.accept()
        print("Connected to: " + str(addr))
        
        conn.send(command.encode())
        print("Command sent: " + command)
        data = conn.recv(1024)
        if data:
            print("Received data: " + data.decode())
    except:
        print("Error connecting to client..retrying")
    s.close()

while True:
    # command = input("Enter command: ")
    command = 'temp'
    send_command(command)