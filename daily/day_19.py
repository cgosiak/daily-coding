# A builder is looking to build a row of N houses that can 
# be of K different colors. He has a goal of minimizing 
# cost while ensuring that no two neighboring houses are 
# of the same color.

# Given an N by K matrix where the nth row and kth column 
# represents the cost to build the nth house with kth color, 
# return the minimum cost which achieves this goal.

# Input -> 
# [
#  [1, 10, 20, 30],
#  [2, 10, 20, 30],
#  [3, 10, 20, 30]
# ]

# Output -> [1, 10, 20] = $31

# Thoughts, this is non-deterministic in polynomial time. So I need to use some fancy approach:
# - Greedy Algorithm (treat it like the knapsack problem)

# We could sort each list, then run through each index and select a cheapest house for that color
from typing import List, Dict
from queue import PriorityQueue
from collections import defaultdict


def efficient_housing(housing_plans: List[List[int]]):
    # color -> house prioritized by cost
    cost_dict: Dict[int, PriorityQueue] = defaultdict(PriorityQueue)
    for house_index in range(len(housing_plans)):
        # iterates through all houses
        for color_index in range(len(housing_plans[house_index])):
            cost_dict[color_index].put((housing_plans[house_index][color_index], house_index))

    # Data is structured, lets run through our options
    selections: List[int] = [None] * len(housing_plans)

    for color, queue in cost_dict.items():
        while queue.qsize() > 0:
            price, house = queue.get()
            if selections[house] is None:
                selections[house] = price
                break

    return sum(selections)

print(efficient_housing([
 [2, 10, 20, 30],
 [1, 10, 20, 30],
 [3, 10, 20, 30]
]))