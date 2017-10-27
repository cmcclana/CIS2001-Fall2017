import unittest
from Checkers import Board

class Test_test1(unittest.TestCase):
    def test_wont_jump_out_of_bound(self):
        board = Board()
        board.add_checker(Board.WHITE, 6,6)
        board.add_checker(Board.BLACK, 7,7)
        board.num_jumps(6,6)

        self.assertEqual(board.max_jumps, 0)

    def test_wont_jump_white_pieces(self):
        board = Board()
        board.add_checker(Board.WHITE, 6,6)
        board.add_checker(Board.WHITE, 5,5)
        board.num_jumps(6,6)

        self.assertEqual(board.max_jumps, 0)


if __name__ == '__main__':
    unittest.main()
