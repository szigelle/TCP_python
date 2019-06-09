import socket

def main():
        HOST = '127.0.0.4'
        PORT = 5004

        SOCKET = socket.socket()
        SOCKET.connect((HOST, PORT))

# prompt user for input, a tumple to be sent to the server
        message = input ("Enter [COMMAND] [key] [value]: ")

        print ('Client: your input was  ' + str(message))

        SOCKET.send(message.encode())

        data = SOCKET.recv(1024).decode()

        print ('Client: msg received from server is:  ' + str(data))

        SOCKET.close()

if __name__ == '__main__':
    main()
