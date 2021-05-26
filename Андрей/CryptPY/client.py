import socket
import pickle
from random import randint

from Encryptor import Encryptor

a = randint(1, 100)
g = None
p = None
B = None

with open('keys.txt', 'r') as f:
    keys = f.read().split()
    p = int(keys[1])
    g = int(keys[3])

sock = socket.socket()
sock.setblocking(1)
port = int(9064)
# inpt = input("1-9064, 2-9067")
# if inpt == 1:
#     port = int(9064)
# else:
#     port = int(9067)
address="localhost"

sock.connect((address, port))

k = 0
encryptor = Encryptor()

print(f"Ключи: a - {a}, p - {p}, g - {g}")


while True:
    A = g ** a % p
    sock.send(pickle.dumps((p, g, A)))
    data = sock.recv(1024)
    k += 1

    if k == 1:
        #print(f"Публичный ключ сервера: {pickle.loads(data)}")
        B = pickle.loads(data)
        secretK = B ** a % p
        print(f"Супер секретный ключ: {secretK}")
    while True:
        sent = input('Введите сообщение: ')
        if sent == 'exit':
            print('Отключение')
            break
        sock.send(pickle.dumps(encryptor.encrypt(sent, secretK)))
        print(f"Зашифрованное сообщение {encryptor.encrypt(sent, secretK)}")