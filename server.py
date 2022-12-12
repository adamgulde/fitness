class ServerSocket: 
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def getlength(self):
        self.sock.recv()

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        self.sock.recv()
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)


import socket
import modify
# server_socket.bind(('10.13.0.16', 3131))
# server_socket.listen() 

filename = 'server_image.png'
server_socket = None

while(True):
    # waits UNTIL file is received to be able to be closed
    # which means can't be closed immediately
    client_connected, client_address = server_socket.accept()
    print(f"Connection request accepted from {client_address[0]},{client_address[1]}")

    write_file = open(filename, 'wb')
    print('Write file opened!')

    client_data = client_connected.recv(2048)
    print('Image received!')

    while len(client_data)>0: 
        # gets hung up here because client data is never 
        # going to zero.. probably because of 
        # while image_chunk in client file
        write_file.write(client_data)
        client_data = client_connected.recv(2048)
    write_file.close()
    print('File written!')
    modify.modify_image(filename)
    print('Image modified!')

    file = open('MOD'+filename, 'rb')
    image_data = file.read(2048)
    while image_data:
        client_connected.send(image_data)
        image_data = file.read(2048)
    file.close()
    print('Image sent!')
# file = open('server_image.png', 'wb')

# image_chunk = client_socket.recv(2048)

# while image_chunk:
#     file.write(image_chunk)
#     image_chunk = client_socket.recv(2048)

# 
client_connected.close()