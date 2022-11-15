import socket
import modify
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('10.13.0.16', 3131))
server.listen()

filename = 'server_image.png'

while(True):
    # waits UNTIL file is received to be able to be closed
    # which means can't be closed immediately
    client_connected, client_address = server.accept()
    print(f"Connection request accepted from {client_address[0]},{client_address[1]}")

    write_file = open(filename, 'wb')
    print('Write file opened!')

    client_data = client_connected.recv(2048)
    print('Image received!')

    while client_data: 
        # gets hung up here because client data is never 
        # going to zero.. probably because of 
        # while image_chunk in client file
        write_file.write(client_data)
        client_data = client_connected.recv(2048)
        print(client_data)
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