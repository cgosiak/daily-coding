"""
Write a program that computes the length of the longest common subsequence of three given strings.
For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious",
it should return 5, since the longest common subsequence is "eieio".
"""

def longest_subsequence(input_string) -> str:
    # use the smallest key because a key longer than the shortest word won't have a match
    sorted_array = sorted(input_string, key=len)

    max_key = sorted_array[0]
    for i in range(len(max_key)):
        for k in range(0, len(max_key), 1):
            print(max_key[i:])
    return ""

print("Longest Subsequence:", longest_subsequence(["epidemiologist", "refrigeration", "supercalifragilisticexpialodocious"]))