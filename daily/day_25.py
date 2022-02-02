from typing import List
import unittest


def fancy_regex(input_str: str, regex: str) -> bool:
    # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        table = [[False] * (len(input_str) + 1) for _ in range(len(regex) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(regex) + 1):
            table[i][0] = table[i - 2][0] and regex[i - 1] == '*'

        for i in range(1, len(regex) + 1):
            for j in range(1, len(input_str) + 1):
                if regex[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                                  (regex[i - 1] == input_str[j - 1] or regex[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if regex[i - 2] == input_str[j - 1] or regex[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]


class TestRegexFunction(unittest.TestCase):

    def test_sub_1_letter_at_end(self):
        input_str: str = "ray"
        regex: str = "ra."
        self.assertTrue(fancy_regex(input_str, regex))

    def test_wildcard_at_beginning_matching_end_of_string(self):
        input_str: str = "chat"
        regex: str = ".*at"
        self.assertTrue(fancy_regex(input_str, regex))

    def test_wildcard_at_beginning_non_matching_end_of_string(self):
        input_str: str = "chats"
        regex: str = ".*at"
        self.assertFalse(fancy_regex(input_str, regex))

    def test_one_or_more_of_specific_char(self):
        input_str: str = "book"
        regex: str = "bo*k"
        self.assertTrue(fancy_regex(input_str, regex))

    def test_0_specific_chars(self):
        input_str: str = "male"
        regex: str = "f*e*male"
        self.assertTrue(fancy_regex(input_str, regex))

    def test_multiple_specific_chars(self):
        input_str: str = "female"
        regex: str = "f*e*male"
        self.assertTrue(fancy_regex(input_str, regex))


if __name__ == "__main__":
    unittest.main()