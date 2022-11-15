import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.13.0.16', 3131))

image_to_upload = open('photo.jpg', 'rb')
image_chunk = image_to_upload.read(2048)
while image_chunk:
    client_socket.send(image_chunk)
    image_chunk = image_to_upload.read(2048)
print('Image transmitted!')
image_to_upload.close()
input('Waiting to continue...')

image_to_save = open('client_save.jpg', 'wb')
server_data = client_socket.recv(2048)
while server_data:
    image_to_save.write(server_data)
    server_data = client_socket.recv(2048)
image_to_save.close()

# ### Client sends photo to server
# file = open('photo.jpg', 'rb')

# image_data = file.read(2048)

# while image_data:
#     clientSocket.send(image_data)
#     image_data = file.read(2048)

# file.close()
client_socket.close()