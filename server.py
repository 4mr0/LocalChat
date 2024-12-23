import socket

def StartServer():
    address = input("Enter address: ")
    port    = int(input("Enter port number: "))

    Server  = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Use internet server
    Server.bind((address,port))
    Server.listen()
    print("Server socket created")

    client, addr = Server.accept()
    print("Client has connected")

    message = "Welcome client!"
    client.send(message.encode())
    while True:
        msg = client.recv(1024).decode()
        if msg == 'quit': break
        else: print(f"Client: {msg}")
        client.send(input("Admin: ").encode())
    client.close()
    Server.close()

if __name__ == '__main__':
    StartServer()
