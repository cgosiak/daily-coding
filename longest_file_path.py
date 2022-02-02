from typing import Dict, List

def is_file(element_name: str) -> bool:
    return len(element_name.split(".")) >= 2

def longest_file_path(file_system_str: str) -> (int, str):
    longest_file_path_str: str = None
    elements: List[str] = file_system_str.split("\n")
    file_system: Dict[int, str] = {}

    for element in elements:
        if is_file(element):
            # Calculate Path
            absolute_path_elements: List[str] = [file_system[x] for x in range(element.count("\t"))]
            absolute_path_elements.append(element.replace("\t", ""))
            absolute_path: str = "/".join(absolute_path_elements)
            if longest_file_path_str is None or len(absolute_path) > len(longest_file_path_str):
                longest_file_path_str = absolute_path
        else:
            # Update Filesystem
            file_system[element.count("\t")] = element.replace("\t", "")

    return longest_file_path_str

tests: Dict[str, int] = {
    "dir\n\tsubdir1\n\tsubdir2": 0,
    "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext": 0,
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext": 32
}

for file_system_str, expected_longest_file_path in tests.items():
    longest_file_path_str = longest_file_path(file_system_str)
    print("Longest File Path:", longest_file_path_str, f"({0 if longest_file_path_str is None else len(longest_file_path_str)})")
