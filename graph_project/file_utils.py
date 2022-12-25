from graph_project.edge import Edge
from graph_project.graph import Graph


class FileUtils:

    def __init__(self):
        pass

    @staticmethod
    def read_graph_from_file(path):
        graph = None
        try:
            with open(path) as f:
                ver_number = int(f.readline())
                is_directed = int(f.readline())

                if is_directed == 0:
                    graph = Graph(ver_number)
                elif is_directed == 1:
                    graph = Graph(ver_number, True)

                for line in f:
                    ver_index_1, ver_index_2, weight = map(int, line.split())
                    graph.add_edge(Edge(ver_index_1, ver_index_2, weight))
        except FileNotFoundError:
            print(f"File isn't found. Check your filepath {path}.")
        return graph

    @staticmethod
    def write_graph_to_file(graph, path):
        ver_number = graph.v()
        is_directed = 0
        if graph.is_directed() is True:
            is_directed = 1
        with open(path, 'w') as f:
            f.write(str(ver_number) + '\n')
            f.write(str(is_directed) + '\n')
            for edge in graph.iter_edges():
                f.write(str(edge.source) + ' ' + str(edge.target) + ' ' + str(edge.weight) + '\n')
