import socket
import time

SERVER_ADDRESS = socket.gethostname()
SERVER_PORT    = 12346

clientsocket = socket.socket()

clientsocket.connect((SERVER_ADDRESS,SERVER_PORT))
message = input("choose your board size: ")
clientsocket.send(message.encode())

while True:
        data = clientsocket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal
        message = input(" -> ")  # again take input
        clientsocket.send(message.encode())  #