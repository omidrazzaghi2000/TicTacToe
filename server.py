import socket
import threading
import time

ADDRESS = socket.gethostname()
PORT    = 12346

client_conn_3x3_array = []
client_conn_4x4_array = []
client_conn_5x5_array = []

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
        
        board_size = int(clientConnection.recv(4).decode())


        if(board_size == 3):
            print("board_size_3 one client added")
            client_conn_3x3_array.append(clientConnection)

        elif(board_size == 4):
            print("board_size_4 one client added")
            client_conn_4x4_array.append(clientConnection)

        elif(board_size == 5):
            print("board_size_5 one client added")
            client_conn_5x5_array.append(clientConnection)





        print(f"new Client with {address}")


def handleClient(board_size):
    if(board_size == 3):
        client_conn_array = client_conn_3x3_array

    elif(board_size == 4):
        client_conn_array = client_conn_4x4_array

    elif(board_size == 5):
        client_conn_array = client_conn_5x5_array
    

    while True:
        while(len(client_conn_array) == 2):
            
            client_conn_array[0].send(f"It is your turn on board {board_size}x{board_size} ... say a cell number".encode())
            
            print(f"Player1 on board {board_size}x{board_size} said {client_conn_array[0].recv(1024)}")

            client_conn_array[1].send(f"It is your turn on board {board_size}x{board_size} ... say a cell number".encode())
            
            print(f"Player2 on board {board_size}x{board_size} said said f{client_conn_array[1].recv(1024)}")

        time.sleep(0.01) 


acceptClients_thread = threading.Thread(target=acceptClients,args=())
acceptClients_thread.start()

threading.Thread(handleClient(3)).start()
threading.Thread(handleClient(4)).start()
threading.Thread(handleClient(5)).start()

acceptClients_thread.join()