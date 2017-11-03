class QueensPuzzle:
    QUEEN = 'Q'
    SPACE = ' '
    def __init__(self, number_of_queens):
        self.number_of_queens_on_board = 0
        self.board = []
        self.total_number_of_solutions = 0
        self.total_queens = number_of_queens
        for row in range(number_of_queens):
            self.board.append([])
            for col in range(number_of_queens):
                self.board[row].append(QueensPuzzle.SPACE)

    def Print(self):
        for row in self.board:
            print('-' * ( len(self.board) * 2 + 1) )
            print('|', end="")
            for character in row:
                print( character, end='|')
            print()
        print('-' * ( len(self.board) * 2 + 1) )
        print()

    def IsRowOpen(self, row_number):
        return not QueensPuzzle.QUEEN in self.board[row_number]

    def IsDownRightDiagonalOpen(self, row_number, col_number):
        while 0 <= row_number < len(self.board) and 0 <= col_number < len(self.board):
            if self.board[row_number][col_number] == QueensPuzzle.QUEEN:
                return False
            row_number -= 1
            col_number -= 1
        return True

    def IsUpRightDiagonalOpen(self, row_number, col_number):
        while 0 <= row_number < len(self.board) and 0 <= col_number < len(self.board):
            if self.board[row_number][col_number] == QueensPuzzle.QUEEN:
                return False
            row_number += 1
            col_number -= 1
        return True

    def CanPlaceQueen(self, row_number, col_number):
        return self.IsRowOpen(row_number) and self.IsDownRightDiagonalOpen(row_number, col_number) and self.IsUpRightDiagonalOpen(row_number, col_number)

    def Solve(self):
        if ( self.number_of_queens_on_board == len(self.board) ):
            self.Print()
            for row in range(len(self.board)):
                for col in range(len(self.board)):
                    if self.board[row][col] == QueensPuzzle.QUEEN:
                        print( "%d" % (row-col), end=" ")
            print()
            self.total_number_of_solutions += 1
        else:
            for row in range(len(self.board)):
                if self.CanPlaceQueen(row, self.number_of_queens_on_board):
                    self.board[row][self.number_of_queens_on_board] = QueensPuzzle.QUEEN
                    self.number_of_queens_on_board += 1
                    self.Solve()
                    self.number_of_queens_on_board -= 1
                    self.board[row][self.number_of_queens_on_board] = QueensPuzzle.SPACE

number_of_queens = int( input("How many queens do you want to try and put on the board?"))
queensPuzzle = QueensPuzzle(number_of_queens)
queensPuzzle.Solve()
print("Total Solutions: %d" % queensPuzzle.total_number_of_solutions )