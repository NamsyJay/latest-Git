
import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 55555))
s.listen()

print("Server is listening!")


while True:
    client, address = s.accept()
    print("Connected to {}".format(address))
    client.send("Welcome To The Server!".encode())
    client.close()