# Run-length encoding is a fast and simple method of encoding strings. 
# The basic idea is to represent repeated successive characters as a 
# single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".


def run_length_encoding(input_str: str) -> str:
    encoded_string: str = ""

    current_char: str = None
    count: int = 0
    for char in input_str:
        if current_char is None:
            current_char = char
        if current_char == char:
            count += 1
        else:
            encoded_string += f"{count}{current_char}"
            current_char = char
            count = 1
    encoded_string += f"{count}{current_char}" # the last counted char

    return encoded_string

print(run_length_encoding("AAAABBBCCDAA"))