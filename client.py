import socket

def StartClient():
    address = input("Enter an IP address: ") # must use an IP the computer knows
    port    = int(input("Enter port number: "))

    Client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Client socket created")
    Client.connect((address, port))
    print("Successfully connected!")

    nick = input("Enter your nickname: ")

    while True:
        server_messages = Client.recv(1045).decode()
        print(server_messages)

        message = input(f"{nick}: ")
        Client.send(message.encode())
        if message == 'exit':
            break

    Client.close()

if __name__ == '__main__':
    StartClient()
