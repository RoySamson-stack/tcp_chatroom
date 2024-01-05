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
            index = cl            

