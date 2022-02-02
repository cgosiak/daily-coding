"""
Given a mapping of digits to letters (as in a phone number), and a digit string, 
return all possible letters the number could represent. You can assume each valid 
number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""

my_dict = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"]
}

def dialer_options(input_str):
    if len(input_str) == 1:
        return my_dict[input_str]
    options = dialer_options(input_str[1:])
    concatenated_options = []
    for letter in my_dict[input_str[0]]:
        concatenated_options.extend([f"{letter}{x}" for x in options])
    return concatenated_options

print("Dialer Options for (23):", dialer_options("232324"))