import socket
import time

SERVER_ADDRESS = socket.gethostname()
SERVER_PORT    = 12346

clientsocket = socket.socket()

clientsocket.connect((SERVER_ADDRESS,SERVER_PORT))

clientsocket.recv

while True:
    time.sleep(1)