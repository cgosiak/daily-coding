"""
Given a string s and an integer k, break up the string into multiple lines such that
each line has a length of k or less. You must break it up so that words don't break
across lines. Each line has to have the maximum possible amount of words. If there's 
no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is 
exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, 
you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No 
string in the list has a length of more than 10.
"""

def get_length_of_line(input_list):
    return len(" ".join(input_list))

def justify_string(input_str: str, line_length: int):
    justified_content = []

    lines_words = []
    for word in input_str.split(" "):
        if len(word) > line_length:
            return []
        if get_length_of_line(lines_words + [word]) <= line_length:
            lines_words.append(word)
        else:
            justified_content.append(lines_words)
            lines_words = [word]

    if len(lines_words) > 0:
        justified_content.append(lines_words)

    return justified_content


justified_content = justify_string("the quick brown fox jumps over the lazy dog", 10)
for line in justified_content:
    print(line)