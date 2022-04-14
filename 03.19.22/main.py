import socket
from pprint import pprint

import threading

HOST = 'localhost'
PORT = 12345


def enc(s):
    return s.encode('utf-8')


def dec(s):
    return s.decode('utf-8')


def new_client(client, address):
    client.send(enc('Connected!'))
    while True:
        recv_msg = client.recv(1024)
        print('\nIncoming msg: \n')
        decoded = dec(recv_msg)
        print('User {0[0]}:{0[1]}:'.format(address), decoded)
        if decoded == 'q':
            break


def main(host, port):
    server = socket.socket()
    server.bind((HOST, PORT))
    server.listen()
    addrs = []
    try:
        while True:
            user, address = server.accept()
            print('Connected: ', address)
            addrs.append(address)
            print('\nNow Connected: \n')
            pprint(addrs)
            threading.Thread(target=new_client,
                             args=(user, address)).start()
    except KeyboardInterrupt:
        print('n\Server shut down!')
        server.close()

    except Exception as e:
        print(e)
        server.close()
    server.close()


if __name__ == "__main__":
    main(HOST, PORT)
