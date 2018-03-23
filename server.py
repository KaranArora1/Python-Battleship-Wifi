
import pbattleship as pbat

'''s = socket.socket()         # Create a socket object

port = 3000                # Reserve a port for your service.
s.bind(('', port))        # Bind to the port

s.listen(1)                 # Now wait for client connection.

while True:
   c, addr = s.accept()     # Establish connection with client.

   message= input("send?")
   if message == 's':
      sys.exit()
   c.send(message.encode('utf-8'))

   message= c.recv(1024)
   print(message.decode('utf-8'))
   
   c.close()                # Close the connection'''

server = pbat.Server()
server.listen(1)
print(server.gethostname())

while True:

   print(server.receive())
   m = input("?")

   server.send(m)








