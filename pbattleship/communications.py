
import socket as s


class Server(s.socket):
    """Sends data between computers for communication: server that is set up
    originally to connect to
    """

    # Initialization
    def __init__(self):

        super().__init__()
        self.port = 3000
        self.bind(('', self.port))

    # Send data via connection
    def send(self, data):

        conn = self.accept()[0]
        conn.send(data.encode('utf-8'))
        conn.close()

    # Receive data via connection
    def receive(self):

        conn = self.accept()[0]
        return conn.recv(1024).decode('utf-8')

    # Return IP address of machine
    def gethostname(self):

        return s.gethostbyname(s.gethostname())


class Client:
    """Sends data between computers for communication: client that is set up
        to connect to server. Doesn't inherit socket class because socket is
        created and destroyed after every connection.
    """

    def __init__(self, host):

        self.socket = s.socket()
        self.host = host
        self.port = 3000

    def send(self, data):

        self.socket.connect((self.host, self.port))
        self.socket.send(data.encode('utf-8'))
        self.socket.close()
        self.socket = s.socket()

    def receive(self):

        self.socket.connect((self.host, self.port))

        message = self.socket.recv(1024).decode('utf-8')

        self.socket.close()
        self.socket = s.socket()

        return message
