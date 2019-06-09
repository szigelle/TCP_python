import socket

def main():
    HOST = "127.0.0.1"
    PORT = 5001

    SOCKET = socket.socket()
    SOCKET.bind((HOST, PORT))

    SOCKET.listen(1)
    connection, address = SOCKET.accept()
    print('SERVER: received connection from [{}]'.format(address))

# infinite while loop over blocking calls to connection.recv()
# reads whatever data client sends and echos using connection.sendall()
# if connection.recv() returns an empty bytes object,
# b'', client closes connection and loop is terminated
    while True:
        data = connection.recv(1024).decode()
        if not data:
            return

        print('...server recieved msg [{}]'.format(data))

        data = 'Hello from SERVER'

        print('...server sending msg - [{}]'.format(data))
        connection.send(data.encode())

    connection.shutdown()
    connection.close()

    print('...SERVER has closed connection')

if __name__ == '__main__':
    main()
