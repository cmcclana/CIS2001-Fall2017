from Checkers import Board

class CheckerFileReader():
    board = Board()
    input = open("input1.txt")
    test_cases = int(input.readline())
    for test_case in range(test_cases):
        board.reset()
        num_white, num_black = input.readline().split()
        for white in range(int(num_white)):
            row, col = input.readline().split()
            board.add_checker(Board.WHITE, int(row), int(col))
        for black in range(int(num_black)):
            row, col = input.readline().split()
            board.add_checker(Board.BLACK, int(row), int(col))
        board.num_jumps(board.first_white_row, board.first_white_col)
