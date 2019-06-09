import socket

def main():
# server hostname or ip
    HOST = '127.0.0.1'

# port used by server
    PORT = 5001

    SOCKET = socket.socket()
    SOCKET.connect((HOST, PORT))

    data = 'Hello from CLIENT!'

    print('...client sending msg - [{}]'.format(data))
#    SOCKET.send((data.encode())
    SOCKET.sendall(data.encode())

#    data = SOCKET.recv(1024).decode()
    data = SOCKET.recv(1024).decode()

    print('CLIENT: msg received from SERVER - [{}]'.format(data))
# Connect has been established and acknowledged by both
# prompt user for input
#    message = input("Enter [COMMAND][,key] [,value]: ")
#    SOCKET.send(message.encode())
#    message = SOCKET.recv(1024).decode()
#    print('CLIENT: msg received from SERVER - [{}]'.format(message))
# keep a loop until server closes the connection

    SOCKET.close()

    print('... Client has closed socket')

if __name__ == '__main__':
    main()
