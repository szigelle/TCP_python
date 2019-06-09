import socket

def main():
# server hostname or ip
    HOST = '127.0.0.1'

# port used by server
    PORT = 5009

    SOCKET = socket.socket()
    SOCKET.connect((HOST, PORT))

    data = 'Hello from CLIENT!'

    print('...client sending msg - [{}]'.format(data))
    SOCKET.sendall(data.encode())

    data = SOCKET.recv(1024).decode()

    print('CLIENT: msg received from SERVER - [{}]'.format(data))

# Connect has been established and acknowledged by both
# prompt user for input
    while True:
        data = input("Enter [command] [key] [value]: ")

        SOCKET.sendall(data.encode())
        data = SOCKET.recv(1024).decode()
        if not data:
            break
        print('CLIENT: msg received from SERVER - [{}]'.format(data))

# keep a loop until server closes the connection
    SOCKET.close()
    print('... client has closed socket')

if __name__ == '__main__':
    main()
