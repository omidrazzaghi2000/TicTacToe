import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton

class TicTacToe(QWidget):
    def __init__(self, n):
        super().__init__()

        self.n = n
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tic Tac Toe')
        self.setGeometry(100, 100, self.n * 100, self.n * 100)

        self.layout = QVBoxLayout()

        self.gridLayout = QGridLayout()
        self.buttons = []

        for i in range(self.n):
            row_buttons = []
            for j in range(self.n):
                button = QPushButton('')
                button.setFixedSize(100, 100)
                button.clicked.connect(lambda _, row=i, col=j: self.on_button_click(row, col))
                row_buttons.append(button)
                self.gridLayout.addWidget(button, i, j)
            self.buttons.append(row_buttons)

        self.layout.addLayout(self.gridLayout)
        self.setLayout(self.layout)

        self.current_player = 'X'

        self.show()

    def on_button_click(self, row, col):
        button = self.buttons[row][col]

        if button.text() == '':
            button.setText(self.current_player)

            if self.check_winner():
                print(f'Player {self.current_player} wins!')
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Check rows
        for i in range(self.n):
            if all(self.buttons[i][j].text() == self.current_player for j in range(self.n)):
                return True

        # Check columns
        for i in range(self.n):
            if all(self.buttons[j][i].text() == self.current_player for j in range(self.n)):
                return True

        # Check diagonals
        if all(self.buttons[i][i].text() == self.current_player for i in range(self.n)):
            return True
        if all(self.buttons[i][self.n - 1 - i].text() == self.current_player for i in range(self.n)):
            return True

        return False

    def reset_board(self):
        for i in range(self.n):
            for j in range(self.n):
                self.buttons[i][j].setText('')
        self.current_player = 'X'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    n = 3  
    boardWindow = TicTacToe(n)

    sys.exit(app.exec_())