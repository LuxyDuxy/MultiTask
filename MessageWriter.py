import os
import time
from typing import NamedTuple
clear = lambda: os.system("cls")
import socket
from threading import Thread

print('Enter your name:')
a = input()

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002
separator_token = "<SEP>"
s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))
clear()
print('wait...')
time.sleep(2)
while True:
    clear()
    to_send = input()
    clear()
    if to_send.lower() == 'q':
        break
    to_send = f"{a}:{to_send}"
    print('sending...')
    time.sleep(2)
    s.send(to_send.encode())
    time.sleep(1)
    clear()
    print('sent')
    time.sleep(2)
    clear()
