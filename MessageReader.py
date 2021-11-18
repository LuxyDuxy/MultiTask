import os
import time
from typing import NamedTuple
clear = lambda: os.system("cls")
import socket
from threading import Thread

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002
separator_token = "<SEP>"
s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))
clear()

def listen_for_messages():
    while True:     
        message = s.recv(1024).decode()
        print(message)
        time.sleep(1)
 
listen_for_messages()
