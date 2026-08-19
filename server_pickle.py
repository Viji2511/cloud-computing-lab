import socket
import pickle
class DataObject:
    def __init__(self, names, values):
        self.names=names
        self.values=values
HOST="127.0.0.1"
PORT=5000
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(1)
print("server is listening")
conn,addr=server.accept()
print("connection by:", addr)
data=conn.recv(4096)
obj=pickle.loads(data)
print("name:", obj.names)
print("values:", obj.values)
total=sum(obj.values)
response=f"Sum={total}"
conn.send(response.encode())
conn.close()
server.close()
