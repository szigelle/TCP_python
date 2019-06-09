import socket

def main():
        HOST = '127.0.0.1'
        PORT = 5000

        SOCKET = socket.socket()
        SOCKET.connect((HOST, PORT))

        message = "Hello from client program!"

        # message needs to contain command, key, value
        print ('Client: send ' + str(message))
        SOCKET.send(message.encode())
        data = SOCKET.recv(1024).decode()

        print ('Client: recv ' + str(data))

        SOCKET.close()

if __name__ == '__main__':
    main()
