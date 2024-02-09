import socket
import time

SERVER_ADDRESS = socket.gethostname()
SERVER_PORT    = 12346

clientsocket = socket.socket()

clientsocket.connect((SERVER_ADDRESS,SERVER_PORT))
board_size=['3','4','5']
message=''
data=''

while(data=="You can not join to the game because this board is full" or message not in board_size):
 message = input("choose your board size: ")
 clientsocket.send(message.encode())
 data=clientsocket.recv(1024).decode()

print(message)

while True:
        data = clientsocket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal
        message = input(" -> ")  # again take input
        clientsocket.send(message.encode())  # send message