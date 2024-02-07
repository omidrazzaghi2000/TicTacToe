import socket
import threading
import time

ADDRESS = socket.gethostname()
PORT    = 12346

client_conn_array = []

def acceptClients():
    #define socket
    serverSocket = socket.socket()

    #bind socket
    serverSocket.bind((ADDRESS,PORT))

    #listen 
    serverSocket.listen(2)

    
    while True:

        print("Waiting for new connection ")

        clientConnection,address = serverSocket.accept()

        client_conn_array.append(clientConnection)

        while(len(client_conn_array) == 2):
            
            client_conn_array[0].send(b"It is your turn ... say a cell number")
            
            print(f"Player1 said f{client_conn_array[0].recv()}")

            client_conn_array[1].send(b"It is your turn ... say a cell number")
            
            print(f"Player2 said f{client_conn_array[1].recv()}")





        print(f"new Client with {address}")

        


acceptClients_thread = threading.Thread(target=acceptClients,args=())
acceptClients_thread.start()
acceptClients_thread.join()