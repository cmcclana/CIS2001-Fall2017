class QueensPuzzle:
    QUEEN = 'Q'
    SPACE = ' '
    def __init__(self, number_of_queens):
        self.number_of_queens_on_board = 0
        self.board = [ [ QueensPuzzle.SPACE ] * number_of_queens ] * number_of_queens
        self.diagonals_minus = [True] * number_of_queens * 2
        self.diagonals_plus = [True] * number_of_queens * 2
        self.rows = [True] * number_of_queens
        self.total_number_of_solutions = 0
        self.total_queens = number_of_queens

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
        return self.rows[row_number]

    def IsDiagonalOpen(self, row_number, col_number):
        return self.diagonals_minus[( row_number - col_number )] and self.diagonals_plus[( row_number + col_number )]

    def CanPlaceQueen(self, row_number, col_number):
        return self.IsRowOpen(row_number) and self.IsDiagonalOpen(row_number, col_number)

    def Solve(self):
        if ( self.number_of_queens_on_board == len(self.board) ):
            # self.Print()
            # for row in range(len(self.board)):
            #     for col in range(len(self.board)):
            #         if self.board[row][col] == QueensPuzzle.QUEEN:
            #             print( "%d" % (row-col), end=" ")
            # print()
            self.total_number_of_solutions += 1
            #print(self.total_number_of_solutions)
        else:
            for row in range(len(self.board)):
                if self.CanPlaceQueen(row, self.number_of_queens_on_board):
                    self.rows[row] = False
                    self.diagonals_minus[(row - self.number_of_queens_on_board )] = False
                    self.diagonals_plus[(row + self.number_of_queens_on_board )] = False
                    self.board[row][self.number_of_queens_on_board] = QueensPuzzle.QUEEN
                    self.number_of_queens_on_board += 1
                    self.Solve()
                    self.number_of_queens_on_board -= 1
                    self.board[row][self.number_of_queens_on_board] = QueensPuzzle.SPACE
                    self.rows[row] = True
                    self.diagonals_minus[(row - self.number_of_queens_on_board )] = True
                    self.diagonals_plus[(row + self.number_of_queens_on_board )] = True

number_of_queens = int( input("How many queens do you want to try and put on the board?"))
queensPuzzle = QueensPuzzle(number_of_queens)
queensPuzzle.Solve()
print("Total Solutions: %d" % queensPuzzle.total_number_of_solutions )