from collections import defaultdict


rectangles = [
    {
        "top_left": (1, 4),
        "dimensions": (3, 3)
    },
    {
        "top_left": (-1, 3),
        "dimensions": (2, 1)
    },
    {
        "top_left": (0, 5),
        "dimensions": (4, 3)
    }
]

def build_rectangle_map(input_set):
    rectangle_map = defaultdict(int)
    for rectangle in rectangles:
        dimensions = rectangle["dimensions"]
        start_x = rectangle["top_left"][0]
        start_y = rectangle["top_left"][1]
        for col in range(dimensions[0]):
            for row in range(dimensions[1]):
                print(row, col)
                rectangle_map[(start_x + col, start_y - row)] += 1
    return rectangle_map


def has_overlapping_rectangles(input_set):
    my_rect_map = build_rectangle_map(input_set)
    print(my_rect_map)
    for rectangle in rectangles:
        found = 0
        dimensions = rectangle["dimensions"]
        start_x = rectangle["top_left"][0]
        start_y = rectangle["top_left"][1]
        for col in range(dimensions[0]):
            for row in range(dimensions[1]):
                if my_rect_map[(start_x + col, start_y - row)] > 1:
                    found += 1
        print(found)
        if (dimensions[0] * dimensions[1]) == found:
            return True
    return False

print("Contains overlapping rectangles:", has_overlapping_rectangles(rectangles))