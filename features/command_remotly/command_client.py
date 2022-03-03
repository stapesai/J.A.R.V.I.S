# receive command from server
def receive_command():
    import socket
    import os

    s = socket.socket()
    hosts = ['192.168.1.11', '192.168.1.12']
    port = 9999

    for host in hosts:
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
            s.close()          
        except:
            print("No incomming connection by server")
            s.close()

if __name__ == "__main__":
    # main function
    print('client program initalized...')
    while True:
        receive_command()
        import time
        time.sleep(10)