'''import socket

host= socket.gethostname()

port= 3000

socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((host, port))


print(socket.recv())
socket.close()'''

#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))


print(s.recv(1024))
s.close()                    # Close the socket when done
