"""
Given a 2D matrix of characters and a target word, write a function that returns whether 
the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. 
Similarly, given the target word 'MASS', you should return true, since it's the last row.
"""

class WordPuzzleBoard(object):

    def __init__(self, board):
        self.board = board

    def _is_letter(self, row, column, letter) -> bool:
        try:
            return self.board[row][column] == letter
        except IndexError:
            return False

    def string_on_board(self, string, direction=None) -> bool:
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self._is_letter(row, column, string[0]):
                    # down
                    if False not in [self._is_letter(row + (i + 1), column, string[i + 1]) for i in range(len(string) - 1)]:
                        return True
                    # right
                    if False not in [self._is_letter(row, column + (i + 1), string[i + 1]) for i in range(len(string) - 1)]:
                        return True
        return False


word_puzzle_board: WordPuzzleBoard = WordPuzzleBoard([
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']
])

print("FOAM", word_puzzle_board.string_on_board("FOAM"))
print("NOB", word_puzzle_board.string_on_board("NOB"))
print("PIG", word_puzzle_board.string_on_board("PIG"))