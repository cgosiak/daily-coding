"""
           a
        /     \
       b      c
        \   /   \
         d       e
          \     /
           \   /
             f
"""
from djikstras import GraphNode, Graph

graph: Graph = Graph()
graph.add_weighted_path('a', 'b', 7)
graph.add_weighted_path('a', 'c', 5)
graph.add_weighted_path('b', 'd', 12)
graph.add_weighted_path('c', 'd', 2)
graph.add_weighted_path('c', 'e', 1)
graph.add_weighted_path('d', 'f', 5)
graph.add_weighted_path('e', 'f', 40)

best_path, total_weight = graph.get_best_path('a', 'f')
print(best_path, total_weight)
