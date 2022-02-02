from typing import List
import math


def format_justified_line(input_str: str, line_length: int) -> str:
    words: List[str] = input_str.split()
    if len(words) > 1:
        default_spacing: str = " " + "".join([" "] * math.floor((line_length - len(input_str)) / (len(words) - 1)))
    else:
        default_spacing = ""

    if len(default_spacing.join(words)) != line_length:
        words[0] += " " # add an extra space for uneven distributions
    return default_spacing.join(words)

def justify_content(words: List[str], line_length: int) -> List[str]:
    justified_content: List[str] = []

    selected_words_for_line: List[str] = []
    for i in range(len(words)):
        current_line: str = " ".join(selected_words_for_line)
        if len(" ".join(selected_words_for_line + [words[i]])) <= line_length:
            selected_words_for_line.append(words[i])
        else:
            justified_content.append(format_justified_line(current_line, line_length))
            selected_words_for_line = [words[i]]
    if len(selected_words_for_line) > 0:
        justified_content.append(format_justified_line(" ".join(selected_words_for_line), line_length))

    return justified_content


justified_content: List[str] = justify_content(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16)
for line in justified_content:
    print(line)
