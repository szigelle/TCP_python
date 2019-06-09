import socket

def Main():
    host = "127.0.0.1"
    port = 5000

    mySocket = socket.socket()
    mySocket.bind((host,port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Server: Connection from " + str(addr))
    data = conn.recv(1024).decode()
    if not data:
        return
    print ("Server: recv " + str(data))

    data = "Hello from Server"

    print ("Server: send " + str(data))
    conn.send(data.encode())

    conn.close()

if __name__ == '__main__':
    Main()
