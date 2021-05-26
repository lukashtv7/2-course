import pickle
import socket
from random import randint

from Encryptor import Encryptor

b = randint(1, 100)
p = None
g = None
A = None

def check(g):
    with open('cert.txt', 'r') as f:
        if str(g) in f.read().split(', '):
            return True
        else:
            return False

print('Server start')
sock = socket.socket()
port = 9064

sock.bind(('', port))
sock.listen(0)

k = 0
encryptor = Encryptor()

port = [9064, 9067]

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    k += 1
    print(f"Это публичные ключи от клиента: {pickle.loads(data)}")
    if k == 1:
        sep = pickle.loads(data)
        p = sep[0]
        g = sep[1]
        print(check(g))
        A = sep[2]
        B = g ** b % p
        print(f"Публичный ключ сервера: {B}")
        conn.send(pickle.dumps(B))
        secretK = A ** b % p
        print(f"А это секретный ключ, для наглядности {secretK}")
    while True:
        data = conn.recv(1024)
        print(f"Зашифрованное сообщение {pickle.loads(data)}")
        cryp = pickle.loads(data)
        print(f"Расшифрованное сообщение {encryptor.decrypt(cryp, secretK)}")

