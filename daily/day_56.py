"""
This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k, write a 
function to determine whether each vertex in the graph can be colored such that no two 
adjacent vertices share the same color using at most k colors.
"""
class AdjacencyMatrix(object):

    def __init__(self, graph):
        self.graph = graph

    def _is_valid(self, graph, color, row, column):
        # Check N, NE, E, SE, S, SW, W, NW
        for row_shift in [-1, 0, 1]:
            for column_shift in [-1, 0, 1]:
                if not (row_shift == 0 and column_shift == 0):
                    check_row = row + row_shift
                    check_column = column + column_shift

                    try:
                        if graph[check_row][check_column] == color:
                            return False
                    except IndexError:
                        continue
        return True

    def _get_uncolored_coords(self, graph):
        for row in range(len(graph)):
            for column in range(len(graph[row])):
                if graph[row][column] == 1:
                    return row, column
        return None

    def get_colored_graph(self, colors, graph=None):
        colored_graph = graph if graph is not None else self.graph
        check_coords = self._get_uncolored_coords(colored_graph)
        if check_coords is None:
            return colored_graph

        row, column = check_coords
        for color in colors:
            if self._is_valid(colored_graph, color, row, column):
                colored_graph[row][column] = color

                if self.get_colored_graph(colors, colored_graph) is not None:
                    return colored_graph

                colored_graph[row][column] = 1

        return None


matrix: AdjacencyMatrix = AdjacencyMatrix([
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
])

graph = matrix.get_colored_graph(['Red', 'Blue', 'Green'])
for row in graph:
    print("\t".join([str(x) for x in row]))
