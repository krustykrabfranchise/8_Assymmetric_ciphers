import socket
import pickle
from keymanager import get_key
HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))
private_key = get_key('private_key.pem')
public_key = get_key('public_key.pem')

sock.send(pickle.dumps(public_key))

server_key = pickle.loads(sock.recv(1024))
print(f'Server public key: {server_key}')

message = b'Hello, world!'
res = bytes([b^server_key[0] for b in message])
sock.send(res)

sock.close()
