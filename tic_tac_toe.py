import random


class TicTacToe:

    def __init__(self):
        self.board = []  # empty board

    def create_board(self):  # creating board by filling each row wise with zeroes
        for i in range(3):
            row = []
            for j in range(3):
                row.append(0)
            self.board.append(row)

    def display_board(self):  # displaying board
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def is_empty(self):  # checking whether board is empty or not
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return True
            return False

    def is_filled(self):  # checking whether board is filled or not
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return False
        return True

    def fill_with(self, x, y, representer):  # filling with 'X' or 'O' w.r.t the given coordinates
        self.board[x][y] = representer

    def check_win(self, representer):  # checking wins in row wise, column wise, diagonal wise

        for i in range(3):
            win = True
            for j in range(3):
                if self.board[i][j] != representer:
                    win = False
                    break

            if win:
                return win

        for i in range(3):
            win = True
            for j in range(3):
                if self.board[j][i] != representer:
                    win = False
                    break

            if win:
                return win

        win = True

        for i in range(3):
            if self.board[i][i] != representer:
                win = False
                break
        if win:
            return win

        win = True

        for i in range(3):
            if self.board[i][2 - i] != representer:
                win = False
                break
        if win:
            return win

        for row in self.board:
            for item in row:
                if item == 0:
                    return False
        return True

    def game_start(self):  # starting game

        self.create_board()
        play_int = random.randint(0, 1)

        while True:

            if play_int == 0:
                player = 'X'
            else:
                player = 'O'

            print("Player {} turn".format(player))
            self.display_board()
            x, y = [int(x) for x in input("Enter two value: ").split()]
            print()
            self.fill_with(x, y, player)
            if self.check_win(player):
                print("Player {} wins".format(player))
                break
            if self.is_filled():
                print("Match Draw")
                break

            play_int = (play_int + 1) % 2

        print()
        self.display_board()


t = TicTacToe()
t.game_start()
