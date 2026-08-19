import socket
import threading
HOST="127.0.0.1"
PORT=5000
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
clients=[]
def broadcast(message,client):
    for c in clients:
        if c!=client:
            c.send(message)
def handle(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message,client)
        except:
            clients.remove(client)
            client.close()
            break
print("server is running")
while True:
    client,address=server.accept()
    print("connection by:", address)
    clients.append(client)
    thread=threading.Thread(target=handle,args=(client,))
    thread.start()