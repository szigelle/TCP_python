import socket

def main():
    HOST = '127.0.0.1'
    PORT = 5000

    SOCKET = socket.socket()
    SOCKET.connect((HOST, PORT))

    message = "Hello from CLIENT!"

    print('CLIENT: sent - [{}]'.format(message))

    SOCKET.send(message.encode())
    message = SOCKET.recv(1024).decod()

    print('CLIENT: received msg from server - [{}]'.format(message))
    SOCKET.close()

if __name___ == '__main__':
    main()
