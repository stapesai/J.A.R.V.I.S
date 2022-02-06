def send_command(command):
    import socket

    s = socket.socket()
    host = '192.168.1.2'
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

# c = input("Enter command: ")
# send_command(c)