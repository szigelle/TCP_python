import socket

def main():
    HOST = "127.0.0.1"
    PORT = 5000

    SOCKET = socket.socket()
    SOCKET.bind((HOST, PORT))

    SOCKET.listen(1)
    connection, address = SOCKET.accept()
    print('SERVER: received connection from [{}]'.format(address))

    message = connection.recv(1024).decode()
    if not message:
        return

    print('SERVER: recieved msg - [{}]'.format(message))

    message = "Hello from SERVER"

    print('SERVER: send msg - [{}]'.format(message))
    connection.send(message.encode())

    connection.shutdown()
    connection.close()

    print('...SERVER has closed connection')

if __name__ == '__main__':
    main()
