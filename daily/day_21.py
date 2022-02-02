# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
from typing import List, Tuple, DefaultDict
from collections import defaultdict


def get_rooms_needed(schedule: List[Tuple[int, int]]) -> int:
    time_slot_needed_rooms: DefaultDict[int, int] = defaultdict(int)
    for entry in schedule:
        for time_slot in range(entry[0], entry[1] + 5, 5):
            time_slot_needed_rooms[time_slot] += 1
    return max(time_slot_needed_rooms.values())

print(get_rooms_needed([(30, 75), (0, 50), (60, 150)]))