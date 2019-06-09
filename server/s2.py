import socket
import kvtest

def main():
    HOST = "127.0.0.1"
    PORT = 5003

    SOCKET = socket.socket()
    SOCKET.bind((HOST, PORT))

    SOCKET.listen(1)
    connection, address = SOCKET.accept()
    print('SERVER: received connection from [{}]'.format(address))

    data = connection.recv(1024).decode()
    if not data:
       return
    print('...server recieved msg [{}]'.format(data))
    data = 'Hello from SERVER'
#    print('...server sending msg - [{}]'.format(data))
    connection.send(data.encode())

# run key value store
    while True:
        data = connection.recv(1024).decode()

        if not data:
            return

        print('...after decoding data, data is: [{}]'.format(data))

        print('... setting data equal to output of kvtest')
        data = kvtest.main(data)
        print('... data after kvtest is [{}]'.format(data))


        if data[0] is None:
            print('... result of kvtest(data) is none')
            connection.send(b'')
            break

        connection.send(data[1].encode())


    connection.close()

    print('...server has closed connection')

if __name__ == '__main__':
    main()
