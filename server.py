import threading
import sockets


host  = '127.0.0.1'
port = '99872'


server = socket.socket(socket.AF_INET. socket.SOCK_STREAM, socket.SOCK_STREAM)
server.bind(host, port)

server.listen()


clients = []
nicknames  = []



def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client = close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat".encode('ascii'))
            nickname.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("Rick".encode('ascii'))

        nickname = client.recv(1024).decode('ascii')

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nicknameof the client is {nickname}!")
        broadcast(f"{nickname} joined the chat".encode('ascii'))
        client.send("Connected to the server".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client))
        thread.start()


print("Server started and is listening ")
receive()        

