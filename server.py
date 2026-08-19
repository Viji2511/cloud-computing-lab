import socket
HOST="127.0.0.1"
PORT=5000
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(1)
print("server is listening")
conn,addr=server.accept()
print("connection by:", addr)
message=conn.recv(1024).decode()
print("client message:", message)
numbers=list(map(int,message.split()))
total=sum(numbers)
conn.send(f"SUm={total}".encode())
conn.close()
server.close()
