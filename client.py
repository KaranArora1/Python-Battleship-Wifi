
import socket               # Import socket module
import sys

s = socket.socket()         # Create a socket object
host = input("What is the hostname of the device you would like to connect to?")
port = 3000               # Reserve a port for your service.

while True:
    s.connect((host, port))

    message= s.recv(1024)
    print(message.decode('utf-8'))

    message= input("Send?")

    if message == 's': sys.exit()
    s.send(message.encode('utf-8'))
    
    s.close()

    s = socket.socket() 
