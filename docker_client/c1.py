import socket

def main():
    HOST = '127.0.0.1'
    PORT = 5000

    SOCKET = socket.socket()
    SOCKET.connect((HOST, PORT))

    message = "Hello from CLIENT!"

    print('CLIENT: sending msg - [{}]'.format(message))

    SOCKET.send(message.encode())
    message = SOCKET.recv(1024).decode()

    print('CLIENT: msg received from SERVER - [{}]'.format(message))

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
