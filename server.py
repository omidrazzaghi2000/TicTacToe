import socket
import threading
import time

ADDRESS = socket.gethostname()
PORT    = 12346

def acceptClients():
    #define socket
    serverSocket = socket.socket()

    #bind socket
    serverSocket.bind((ADDRESS,PORT))

    #listen 
    serverSocket.listen(2)

    #always waiting for connection

    while True:
        print("Waiting for new connection ")

        clientConnection,address = serverSocket.accept()

        print(f"new Client with {address}")


acceptClients_thread = threading.Thread(target=acceptClients,args=())
acceptClients_thread.start()


while True:
    time.sleep(1)