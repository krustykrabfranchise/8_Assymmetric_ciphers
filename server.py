import socket
import pickle
from keymanager import get_key


HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)

conn, addr = sock.accept()
print(f"Server is running on {host}:{port}")

private_key = get_key("private.pem")
public_key = get_key("public.pem")

client_key = pickle.loads(conn.recv(1024))
print(f"Client public key: {client_key}")

conn.send(pickle.dumps(public_key))

encrypted_message = conn.recv(1024)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = bytes([b^private_key[0] for b in encrypted_message])
print(f"Decrypted message: {decrypted_message.decode()}")

conn.close()
