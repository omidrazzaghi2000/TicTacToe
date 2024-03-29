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

    #option [Address already in used error]
    serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    #bind socket
    serverSocket.bind((ADDRESS,PORT))

    #listen 
    serverSocket.listen(2)

    
    while True:

        print("Waiting for new connection ")

        clientConnection,address = serverSocket.accept()
        
        

        while True:

            board_size = int(clientConnection.recv(4).decode())

            if(board_size == 3):
                
                #check that game is on or off
                if len(client_conn_3x3_array) == 2:
                    clientConnection.send(b"You can not join to the game because this board is full")
                    continue
                    

                print("board_size_3 one client added")
                client_conn_3x3_array.append(clientConnection)
                clientConnection.send(b"Joined the game successfully")
                break

            elif(board_size == 4):

                #check that game is on or off
                if len(client_conn_4x4_array) == 2:
                    clientConnection.send(b"You can not join to the game because this board is full")
                    continue

                print("board_size_4 one client added")
                client_conn_4x4_array.append(clientConnection) 
                clientConnection.send(b"Joined the game successfully")
                break

            elif(board_size == 5):

                #check that game is on or off
                if len(client_conn_5x5_array) == 2:
                    clientConnection.send(b"You can not join to the game because this board is full")
                    continue

                print("board_size_5 one client added")
                client_conn_5x5_array.append(clientConnection)
                clientConnection.send(b"Joined the game successfully")
                break



        print(f"new Client with {address}")


def handleClient(board_size,client_conn_array):

    
    client_message = None

    while True:
        while(len(client_conn_array) == 2):
            
            if client_message == None: # it is the first time that server is in this loop
                client_conn_array[0].send(f"None,None^It is your turn on board {board_size}x{board_size} ... say a cell number".encode())
            else:
                row = client_message.split(",")[0]
                col = client_message.split(",")[1]
                client_conn_array[0].send(f"{row},{col}^It is your turn on board {board_size}x{board_size} ... say a cell number".encode())

            client_message = client_conn_array[0].recv(1024).decode()
            
            print(f"Player1 on board {board_size}x{board_size} said {client_message}")

            row = client_message.split(",")[0]
            col = client_message.split(",")[1]

            client_conn_array[1].send(f"{row},{col}^It is your turn on board {board_size}x{board_size} ... say a cell number".encode())
            
            client_message = client_conn_array[1].recv(1024).decode()

            print(f"Player2 on board {board_size}x{board_size} said said {client_message}")

        time.sleep(0.01) 


acceptClients_thread = threading.Thread(target=acceptClients,args=())
acceptClients_thread.start()

threading.Thread(target=handleClient,args=(3,client_conn_3x3_array)).start()
threading.Thread(target=handleClient,args=(4,client_conn_4x4_array)).start()
threading.Thread(target=handleClient,args=(5,client_conn_5x5_array)).start()

#for not finishing main thread
while True:
    time.sleep(1)