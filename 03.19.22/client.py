import socket
from main import HOST, PORT, enc, dec

client = socket.socket()
client.connect((HOST, PORT))
try:
    msg = client.recv(1024)
    print('\nIncoming msg: \n')
    print(dec(msg))
    while True:
        msg = input('\nType ur msg: \n')
        client.send(enc(msg))
        if msg == 'q':
            break

except KeyboardInterrupt:
    print('n\Client shut down!')
    client.send(enc('q'))
    client.close()
except Exception as e:
    print(e)
    client.close()
client.close()
