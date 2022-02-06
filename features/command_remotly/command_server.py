
def send_command(command):
    import time
    import socket
    import sys
    import os

    s = socket.socket()
    host = '192.168.1.5'
    port = 9999
    
    command = input("Enter command: ")

    try:
        s.bind((host, port))
        print("Listening for connections...")
        s.listen(1)
        conn, addr = s.accept()
        print("Connected to: " + str(addr))
        
        conn.send(command.encode())
        print("Command sent: " + command)
    except:
        print("Error connecting to client..retrying")
    s.close()