from typing import Dict, Deque
from collections import deque, defaultdict


class GraphNode(object):

    def __init__(self, name: str):
        self.name: str = name
        self.children = []
        self.weights: Dict[str, int] = {}
        self.optimal_weight: int or None = None
        self.optimal_parent = None
        self.visited: bool = False

    def reset(self):
        self.optimal_parent = None
        self.optimal_weight = None
        self.visited = False

    def add_weighted_path(self, child_node, weight: int):
        self.weights[child_node.name] = weight
        self.children.append(child_node)

    def visit_from(self, parent_node):
        visiting_weight: int = parent_node.optimal_weight + self.weights[parent_node.name]
        if self.optimal_weight is None or visiting_weight < self.optimal_weight:
            self.optimal_weight = visiting_weight
            self.optimal_parent = parent_node

    def get_unvisited_children(self):
        return [node for node in self.children if not node.visited]


class Graph(object):

    def __init__(self):
        self.nodes: Dict[str, GraphNode] = {}

    def add_weighted_path(self, starting_node_name: str, destination_node_name: str, weight: int):
        if starting_node_name not in self.nodes:
            self.nodes[starting_node_name] = GraphNode(starting_node_name)
        if destination_node_name not in self.nodes:
            self.nodes[destination_node_name] = GraphNode(destination_node_name)

        self.nodes[starting_node_name].add_weighted_path(self.nodes[destination_node_name], weight)
        self.nodes[destination_node_name].add_weighted_path(self.nodes[starting_node_name], weight)

    def get_best_path(self, starting_node_name: str, destination_node_name: str):
        nodes_to_visit: Deque = deque([self.nodes[starting_node_name]])

        while len(nodes_to_visit) > 0:
            visiting_node: GraphNode = nodes_to_visit.popleft()
            if visiting_node.name == starting_node_name:
                visiting_node.optimal_weight = 0
            for child_node in visiting_node.get_unvisited_children():
                child_node.visit_from(visiting_node)
                nodes_to_visit.append(child_node)
            visiting_node.visited = True

        path: List[GraphNode] = [self.nodes[destination_node_name]]
        while path[len(path) - 1].optimal_parent is not None:
            path.append(path[len(path) - 1].optimal_parent)

        return [x.name for x in path][::-1], self.nodes[destination_node_name].optimal_weight
