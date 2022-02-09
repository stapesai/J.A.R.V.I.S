# send command
def send_command(command):
    import socket

    s = socket.socket()
    hosts = ['192.168.1.11', '192.168.1.12']
    port = 9999

    for host in hosts:
        try:
            s.bind((host, port))
            print("Listening for connections...")
            s.listen(2)

            conn, addr = s.accept()
            print("Connected to: " + str(addr))
            
            conn.send(command.encode())
            print("Command sent: " + command)

            global reply
            reply = conn.recv(1024).decode()
            print("Reply received: " + reply)
            s.close()
            return reply
            
        except:
            print("Error connecting to client..retrying")
        s.close()


# check connection
def check_connection_to_client():
    import socket

    s = socket.socket()
    hosts = ['192.168.1.11', '192.168.1.12']
    port = 9999

    while True:
        for host in hosts:
            try:
                s.bind((host, port))
                s.listen(2)
                conn, addr = s.accept()
                print("Connected to: " + str(addr))
                s.close()
                return True
                
            except:
                print("can't connect to client, retrying")
                s.close()
                import time
                time.sleep(1)

command = input("Enter command: ")
send_command(command)