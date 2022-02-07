def receive_command():
    import socket
    import os

    s = socket.socket()
    host = '192.168.1.2' or '192.168.1.3'
    port = 9999

    try:
        s.connect((host, port))
        print("Connected to server")
        
        command = s.recv(1024).decode()
        print(f"Command Received : '{command}' ...")
        
        if command == 'shutdown':
            s.send('shutting down sir'.encode())
            print("Shutting down...")
            os.system('shutdown -s -t 0')
        
        else:
            s.send('command received'.encode())
                
    except:
        print("No incomming connection by server")

while True:
    receive_command()
    import time
    # time.sleep(10)