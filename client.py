import socket
import time
from PyQt5.QtWidgets import QApplication
import sys
import os
from boardgui import TicTacToe
import threading

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
boardWindow = None
def run_application(n):
        global boardWindow
        app = QApplication(sys.argv)
        boardWindow = TicTacToe(n)
        boardWindow.disable_user_action
        os._exit(app.exec_())
threading.Thread(target=run_application,args=(int(message),)).start()
while True:
        if(boardWindow != None):
                #define board 
                boardWindow:TicTacToe = boardWindow
                boardWindow.top_label.setText("Wait for player")

                if boardWindow.sock_client == None:
                        boardWindow.define_socket(clientsocket)
                
                
                boardWindow.disable_user_action()

                data = clientsocket.recv(1024).decode() 
                print('Received from server: ' + data) 

                opponet_row = data.split("^")[0].split(",")[0]
                opponet_col = data.split("^")[0].split(",")[1]
                if(opponet_row != 'None' and opponet_col != 'None'):
                        row = int(opponet_row)
                        col = int(opponet_col)
                        boardWindow.on_button_click(row,col)
                boardWindow.isPicked = False
                boardWindow.enable_user_action()
                
                


                # wait for click on a cell on the board 
                while(not boardWindow.isPicked):
                      time.sleep(0.5)#cpu usage
                
                boardWindow.disable_user_action()

                clientsocket.send(f"{boardWindow.current_selected_row},{boardWindow.current_selected_col}".encode())  # send choosen cell address to server