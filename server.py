import socket
import threading
import time

ADDRESS = socket.gethostname()
PORT_3X3    = 12346
PORT_4X4    = 12347
PORT_5X5    = 12348

client_conn_array_3x3 = []
client_conn_array_4x4 = []
client_conn_array_5x5 = []

def acceptClients(board_size):
    #define socket
    serverSocket = socket.socket()

    #reuse address option
    serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    #bind socket
    if board_size == 3:
        serverSocket.bind((ADDRESS,PORT_3X3))
    elif board_size == 4:
        serverSocket.bind((ADDRESS,PORT_4X4))
    elif board_size == 5:
        serverSocket.bind((ADDRESS,PORT_5X5))

    #listen 
    serverSocket.listen(2)

    
    while True:

        print(f"Waiting for new connection for board size : {board_size}")

        clientConnection,address = serverSocket.accept()

        if(board_size == 3):
            client_conn_array = client_conn_array_3x3
        elif(board_size == 4):
            client_conn_array = client_conn_array_4x4
        elif(board_size == 5):
            client_conn_array = client_conn_array_5x5

        client_conn_array.append(clientConnection)

        while(len(client_conn_array) == 2):
            
            client_conn_array[0].send(f"It is your turn on board {board_size}x{board_size} ... say a cell number".encode())
            
            print(f"Player1 on board {board_size}x{board_size} said {client_conn_array[0].recv(1024).decode()}")

            client_conn_array[1].send(f"It is your turn on board {board_size}x{board_size} ... say a cell number".encode())
            
            print(f"Player2 on board {board_size}x{board_size} said {client_conn_array[1].recv(1024).decode()}")


        print(f"new Client with {address}")




        


acceptClients3x3_thread = threading.Thread(target=acceptClients,args=(3,))
acceptClients3x3_thread.start()
acceptClients4x4_thread = threading.Thread(target=acceptClients,args=(4,))
acceptClients4x4_thread.start()
acceptClients5x5_thread = threading.Thread(target=acceptClients,args=(5,))
acceptClients5x5_thread.start()
acceptClients3x3_thread.join()
acceptClients4x4_thread.join()
acceptClients5x5_thread.join()