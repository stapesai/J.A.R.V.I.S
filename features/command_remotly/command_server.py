def send_command(command):
    import socket

    s = socket.socket()
    host = '192.168.1.2' or '192.168.1.3'
    port = 9999

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
        
    except:
        print("Error connecting to client..retrying")
    s.close()

def check_connection_to_client():
    import socket

    s = socket.socket()
    host = '192.168.1.2' or '192.168.1.3'
    port = 9999

    while True:
        try:
            s.bind((host, port))
            print("Connected to client")
            s.close()
            break
        except:
            print("can't connect to client, retrying")
            import time
            # time.sleep(5)
    
# c = input("Enter command: ")
# send_command(c)

check_connection_to_client()