from typing import List, Set, Dict
from collections import deque
from time import time

class Node(object):

    def __init__(self, value: int):
        self.value: int = value
        self.left = None
        self.right = None


class Graph(object):

    def __init__(self, values: List[int]):
        self.values: List[int] = values
        self.root: Node = self.list_to_bst(values)

    def list_to_bst(self, given_list: List[int]) -> Node:
        if not given_list:
            return None
        mid_point: int = len(given_list) // 2
        node: Node = Node(given_list[mid_point])
        node.left = self.list_to_bst(given_list[:mid_point])
        node.right = self.list_to_bst(given_list[mid_point+1:])
        return node

    def breadth_first_search(self) -> List[int]:
        # USE A DEQUE (double ended queue)
        queue = deque([self.root])
        order = []

        while queue:
            current_node: Node = queue.popleft()
            order.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return order

    def depth_first_search(self) -> List[int]:
        return self._depth_first_search(self.root)

    def _depth_first_search(self, node: Node) -> List[int]:
        if node is None:
            return []

        order: List[int] = [node.value]
        order.extend(self._depth_first_search(node.left))
        order.extend(self._depth_first_search(node.right))
        return order


values: List[int] = [1, 2, 3, 4, 5, 6, 7]
graph: Graph = Graph(values)

# Graph View
#         4
#      /     \
#     2       6
#    / \     / \
#   1   3   5   7
print("Breadth First Search:\t", graph.breadth_first_search())
print("Depth First Search:\t", graph.depth_first_search())

# Doing Measurements
# print("Array Size,GRAPH,BFS,DFS")
# for arr_size in range(100000, 1100000, 100000):
#     values: List[int] = [x for x in range(arr_size)]
#     build_graph_start = time()
#     graph: Graph = Graph(values)
#     build_graph_time = time() - build_graph_start

#     # BFS
#     bfs_start = time()
#     graph.breadth_first_search()
#     bfs_time = time() - bfs_start

#     # DFS
#     dfs_start = time()
#     graph.depth_first_search()
#     dfs_time = time() - dfs_start
    
#     # Print Results
#     print(arr_size, build_graph_time, bfs_time, dfs_time)
