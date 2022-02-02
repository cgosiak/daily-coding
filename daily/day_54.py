"""
Soduko Solver
"""

class SodukoBoard(object):

    def __init__(self, board):
        self.board = board

    def print_board(self):
        for i in range(len(self.board)):
            row = self.board[i]
            if i % 3 == 0:
                print("-------------------------")
            print(f"| {row[0]} {row[1]} {row[2]} | {row[3]} {row[4]} {row[5]} | {row[6]} {row[7]} {row[8]} |")
        print("-------------------------")

    def is_valid(self, number: int, row: int, column: str) -> bool:
        # Check Row
        for i in range(len(self.board[row])):
            if self.board[row][i] == number and i != column:
                return False
        
        # Check Column
        for i in range(len(self.board)):
            if self.board[i][column] == number and i != row:
                return False

        # Check Box
        box_start_row: int = row // 3
        box_start_column: int = column // 3

        for check_row in range((box_start_row * 3), (box_start_row * 3 + 3)):
            for check_column in range((box_start_column * 3), (box_start_column * 3 + 3)):
                if self.board[check_row][check_column] == number and check_row != row and check_column != column:
                    return False
        
        return True

    def _get_empty_cell(self):
        for i in range(len(self.board)):
            for k in range(len(self.board[i])):
                if self.board[i][k] == 0:
                    return (i, k)
        return None

    def solve(self):
        empty_cell = self._get_empty_cell()

        if empty_cell is None:
            return True

        row, column = empty_cell

        for i in range(1, 10):
            if self.is_valid(i, row, column):
                self.board[row][column] = i

                if self.solve():
                    return True

                self.board[row][column] = 0
        
        return False


suduko: SodukoBoard = SodukoBoard([
    [0, 0, 0, 0, 6, 1, 4, 0, 3],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 3, 0, 0, 0, 6, 0],
    [0, 0, 7, 0, 0, 2, 0, 0, 0],
    [3, 0, 0, 7, 0, 5, 0, 0, 2],
    [0, 0, 0, 1, 0, 0, 0, 5, 0],
    [0, 0, 0, 0, 0, 4, 1, 3, 0],
    [8, 0, 0, 0, 5, 0, 0, 4, 0],
    [0, 0, 9, 0, 0, 0, 0, 0, 0]
])

suduko.solve()
suduko.print_board()
