class Board():
    BLACK = 'b'
    WHITE = 'w'
    EMPTY = ' '

    def __init__(self):
        self.reset()
        self.max_jumps = 0
        self.current_jumps = 0
        self.first_white_row = -1
        self.first_white_col = -1

    def reset(self):
        self.board = []
        for row in range(8):
            self.board.append([])
            for col in range(8):
                self.board[row].append(Board.EMPTY)

    def add_checker(self, color, row, col):
        if row < 0 or row > len(self.board) or col < 0 or col > len(self.board[row]):
            raise IndexError
        self.board[row][col] = color
        if self.first_white_row == -1 and color == Board.WHITE:
            self.first_white_row = row
            self.first_white_col = col

    def print(self):
        for row in range(len(self.board)):
            print('-'*17)
            print('|', end="")
            for col in range(len(self.board[row])):
                print(self.board[row][col], end="|")
            print()
        print('-'*17)

    def num_jumps(self, row, col):
        # up left - row -2 , col -2
        if row-2 >= 0 and col - 2 >= 0 and self.board[row-1][col-1] == Board.BLACK and self.board[row-2][col-2] == Board.EMPTY:
            self.board[row][col] = Board.EMPTY
            self.board[row-1][col-1] = Board.EMPTY
            self.board[row-2][col-2] = Board.WHITE
            self.current_jumps += 1
            if self.current_jumps > self.max_jumps:
                self.max_jumps = self.current_jumps
            self.num_jumps(row-2, col-2)
            self.current_jumps -= 1
            self.board[row-2][col-2] = Board.EMPTY
            self.board[row-1][col-1] = Board.BLACK
            self.board[row][col] = Board.WHITE

        # up right - row -2 , col +2
        if row-2 >= 0 and col + 2 < 8 and self.board[row-1][col+1] == Board.BLACK and self.board[row-2][col+2] == Board.EMPTY:
            self.board[row][col] = Board.EMPTY
            self.board[row-1][col+1] = Board.EMPTY
            self.board[row-2][col+2] = Board.WHITE
            self.current_jumps += 1
            if self.current_jumps > self.max_jumps:
                self.max_jumps = self.current_jumps
            self.num_jumps(row-2, col+2)
            self.current_jumps -= 1
            self.board[row-2][col+2] = Board.EMPTY
            self.board[row-1][col+1] = Board.BLACK
            self.board[row][col] = Board.WHITE

        # down right - row +2 , col +2
        if row+2 < 8 and col + 2 < 8 and self.board[row+1][col+1] == Board.BLACK and self.board[row+2][col+2] == Board.EMPTY:
            self.board[row][col] = Board.EMPTY
            self.board[row+1][col+1] = Board.EMPTY
            self.board[row+2][col+2] = Board.WHITE
            self.current_jumps += 1
            if self.current_jumps > self.max_jumps:
                self.max_jumps = self.current_jumps
            self.num_jumps(row+2, col+2)
            self.current_jumps -= 1
            self.board[row+2][col+2] = Board.EMPTY
            self.board[row+1][col+1] = Board.BLACK
            self.board[row][col] = Board.WHITE

        # down left - row +2 , col -2
        if row+2 < 8 and col - 2 >= 0 and self.board[row+1][col-1] == Board.BLACK and self.board[row+2][col-2] == Board.EMPTY:
            self.board[row][col] = Board.EMPTY
            self.board[row+1][col-1] = Board.EMPTY
            self.board[row+2][col-2] = Board.WHITE
            self.current_jumps += 1
            if self.current_jumps > self.max_jumps:
                self.max_jumps = self.current_jumps
            self.num_jumps(row+2, col-2)
            self.current_jumps -= 1
            self.board[row+2][col-2] = Board.EMPTY
            self.board[row+1][col-1] = Board.BLACK
            self.board[row][col] = Board.WHITE

        if row == self.first_white_row and col == self.first_white_col and self.current_jumps == 0:
            print("The max number of jumps is:", self.max_jumps)


#board = Board()
#board.add_checker('w', 3, 3)
#board.add_checker('b', 4, 4)
#board.add_checker('b', 6, 4)
#board.add_checker('b', 6, 2)
#board.print()
#board.num_jumps(3,3)

