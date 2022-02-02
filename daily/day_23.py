from typing import List, Tuple, Deque, Set
from queue import deque


def distance_between_pts(input_map: List[List[bool]], starting_location: Tuple[int], ending_location: Tuple[int]) -> int:
    # Setup a data structure for keeping track of visited cells
    visited_cells: Set[Tuple[int]] = set()

    # Setup a queue for BFS, initialize it with the starting point
    cell_queue: Deque[Tuple[int]] = deque()
    cell_queue.append(starting_location)

    # Set starting cell distance to 0
    input_map[starting_location[0]][starting_location[1]] = 0

    while cell_queue:
        current_cell: Tuple = cell_queue.popleft()
        current_row, current_column = current_cell
        current_value: int = input_map[current_row][current_column]

        # Setup neighbors
        neighbors: List[Tuple] = [
            (current_row - 1, current_column), # North
            (current_row, current_column + 1), # East
            (current_row + 1, current_column), # South
            (current_row, current_column - 1)  # West
        ]

        # Loop through neighbors
        for neighboring_cell in neighbors:
            neighboring_row, neighboring_column = neighboring_cell
            if neighboring_row < 0 or neighboring_row >= len(input_map) or neighboring_column < 0  or neighboring_column >= len(input_map[neighboring_row]):
                continue # early exit if the cell does not exist
            neighboring_value = input_map[neighboring_row][neighboring_column]

            # check if cell has been assigned already or is wall
            if type(neighboring_value) == bool:
                if neighboring_value:
                    visited_cells.add(neighboring_cell)
                    continue # leave walls as is
                else:
                    input_map[neighboring_row][neighboring_column] = current_value + 1
            else:
                if (current_value + 1) < neighboring_value:
                    input_map[neighboring_row][neighboring_column] = current_value + 1

            if neighboring_cell not in visited_cells:
                cell_queue.append(neighboring_cell)

        visited_cells.add(current_cell)

    ending_cell_value = input_map[ending_location[0]][ending_location[1]]
    return ending_cell_value if type(ending_cell_value) != bool else None


print(
    distance_between_pts([
        [False, False, False, False],
        [True,  True,  False, True ],
        [False, False, False, False],
        [False, False, False, False]
    ], (3, 0), (0, 0)
))

print(
    distance_between_pts([
        [False, False, False, False],
        [True,  True,  False, True ],
        [False, False, False, False],
        [False, False, False, False]
    ], (1, 2), (0, 0)
))