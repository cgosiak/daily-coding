from collections import deque
from typing import Deque

class Node(object):

	def __init__(self, name):
		self.name = name
		self.visited = False
		self.children = set()
		self.costs = {}
		self.optimal_cost = None
		self.optimal_parent_node = None

	def add_child(self, child, cost):
		self.children.add(child)
		self.costs[child] = cost

	def visit_from(self, parent):
		total_cost = parent.optimal_cost + self.costs[parent]
		if not self.optimal_parent_node or total_cost < self.optimal_cost:
			self.optimal_parent_node = parent
			self.optimal_cost = total_cost

	def get_unvisited_children(self):
		return [x for x in self.children if not x.visited]

class Graph(object):

	def __init__(self):
		self.nodes = {}

	def add_path(self, node_1, node_2, cost):
		if node_1 not in self.nodes:
			self.nodes[node_1] = Node(node_1)
		if node_2 not in self.nodes:
			self.nodes[node_2] = Node(node_2)
		self.nodes[node_1].add_child(self.nodes[node_2], cost)
		self.nodes[node_2].add_child(self.nodes[node_1], cost)

	def breadth_first_search(self, starting_node):
		queue: Deque = deque([self.nodes[starting_node]])
		path = [self.nodes[starting_node]]

		while queue:
			current_node = queue.popleft()
			if current_node not in path:
				path.append(current_node)
			queue.extend(current_node.get_unvisited_children())
			current_node.visited = True

		return [x.name for x in path]

	def dijkstras(self, starting_node, ending_node):
		queue: Deque = deque([self.nodes[starting_node]])
		self.nodes[starting_node].optimal_cost = 0
		while queue:
			current_node = queue.popleft()
			for child_node in current_node.get_unvisited_children():
				child_node.visit_from(current_node)
				queue.append(child_node)
			current_node.visited = True

		reversed_optimal_path = [self.nodes[ending_node].name]
		current_node = self.nodes[ending_node]
		while current_node.optimal_parent_node:
			reversed_optimal_path.append(current_node.optimal_parent_node.name)
			current_node = current_node.optimal_parent_node
		optimal_route_cost = self.nodes[ending_node].optimal_cost

		return reversed_optimal_path[::-1], optimal_route_cost

# Simple Graph
# A -> B: 5
# B -> C: 2
# graph = Graph()
# graph.add_path("A", "B", 5)
# graph.add_path("B", "C", 2)

# print(graph.dijkstras("A", "C"))

# Complex Graph
# A -> B: 5
# A -> C: 10
# B -> C: 2
# C -> D: 4
graph = Graph()
graph.add_path("A", "B", 5)
graph.add_path("A", "C", 10)
graph.add_path("B", "C", 2)
graph.add_path("C", "D", 4)

print(graph.dijkstras("A", "D"))