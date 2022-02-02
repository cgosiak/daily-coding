# The edit distance between two strings refers to the minimum 
# number of character insertions, deletions, and substitutions 
# required to change one string to the other. For example, the 
# edit distance between “kitten” and “sitting” is three: 
# substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
import unittest


def edit_distance(str_1: str, str_2: str) -> int:
    word_matrix: List[List[int]] = [[None for x in range(len(str_1) + 1)] for y in range(len(str_2) + 1)]
    # prefill known values
    word_matrix[0] = [x for x in range(0, len(str_1) + 1)]
    for i in range(0, len(str_2) + 1):
        word_matrix[i][0] = i

    for row in range(1, len(str_2) + 1):
        for column in range(1, len(str_1) + 1):
            word_matrix[row][column] = min([
                word_matrix[row-1][column-1] if str_2[row-1] == str_1[column-1] else word_matrix[row-1][column-1] + 1,
                word_matrix[row][column-1] + 1,
                word_matrix[row-1][column] + 1
            ])
    print(word_matrix)
    return word_matrix[-1][-1]


class TestEditDistance(unittest.TestCase):

    def test_1(self):
        self.assertEquals(edit_distance('cat', 'cat'), 0)

    def test_2(self):
        self.assertEquals(edit_distance('kitten', 'sitting'), 3)

    def test_3(self):
        self.assertEquals(edit_distance('female', 'finale'), 2)

    def test_4(self):
        self.assertEquals(edit_distance('', 'test'), 4)


if __name__ == "__main__":
    unittest.main()
