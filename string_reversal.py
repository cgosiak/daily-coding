def reverse_string(input_str: str) -> str:
    return "".join(reversed(input_str))

def reverse_string_as_array(input_str: str) -> str:
    return input_str[::-1]

print(reverse_string("Caleb"))
print(reverse_string_as_array("Caleb"))