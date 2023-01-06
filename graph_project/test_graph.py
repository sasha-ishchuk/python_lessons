import random

import pytest
from graph_project.edge import Edge
from graph_project.graph import Graph


def test_v():
    assert Graph().v() == 0
    assert Graph(5).v() == 5


def test_e():
    assert Graph(4).e() == 0

    # undirected graph
    graph = Graph(5)
    graph.add_edge(Edge(1, 4, random.randint(1, 10)))
    graph.add_edge(Edge(2, 1, random.randint(1, 10)))
    graph.add_edge(Edge(1, 2, random.randint(1, 10)))
    assert graph.e() == 2

    # directed graph
    graph = Graph(5, True)
    graph.add_edge(Edge(1, 4, random.randint(1, 10)))
    graph.add_edge(Edge(2, 1, random.randint(1, 10)))
    graph.add_edge(Edge(1, 2, random.randint(1, 10)))
    assert graph.e() == 3


def test_is_directed():
    assert Graph(5).is_directed() is False
    assert Graph(5, True).is_directed() is True


def test_add_node():
    assert Graph(5).add_node(4) is True
    assert Graph(5).add_node(5) is False


def test_has_node():
    assert Graph(5).has_node(4) is True
    assert Graph(5).has_node(5) is False


def test_add_edge():
    # undirected graph
    graph = Graph(5)
    graph.add_edge(Edge(1, 4, random.randint(1, 10)))
    graph.add_edge(Edge(2, 1, random.randint(1, 10)))
    assert graph.e() == 2

    graph.add_edge(Edge(1, 3, random.randint(1, 10)))
    assert graph.e() == 3

    # directed graph
    graph = Graph(5, True)
    graph.add_edge(Edge(1, 4, random.randint(1, 10)))
    graph.add_edge(Edge(2, 1, random.randint(1, 10)))
    assert graph.e() == 2

    graph.add_edge(Edge(1, 2, random.randint(1, 10)))
    graph.add_edge(Edge(4, 1, random.randint(1, 10)))
    assert graph.e() == 4


def test_has_edge():
    # undirected graph
    graph = Graph(5)
    graph.add_edge(Edge(1, 4, random.randint(1, 10)))
    graph.add_edge(Edge(2, 1, random.randint(1, 10)))

    assert graph.has_edge(Edge(1, 4)) is True
    assert graph.has_edge(Edge(4, 1)) is True
    assert graph.has_edge(Edge(1, 2)) is True
    assert graph.has_edge(Edge(2, 1)) is True
    assert graph.has_edge(Edge(2, 3)) is False

    # directed graph
    graph = Graph(5, True)
    graph.add_edge(Edge(1, 4, random.randint(1, 10)))
    graph.add_edge(Edge(2, 1, random.randint(1, 10)))

    assert graph.has_edge(Edge(1, 4)) is True
    assert graph.has_edge(Edge(4, 1)) is False
    assert graph.has_edge(Edge(1, 2)) is False
    assert graph.has_edge(Edge(2, 1)) is True
    assert graph.has_edge(Edge(3, 2)) is False


def test_del_edge():
    # undirected graph
    graph = Graph(5)
    graph.add_edge(Edge(1, 4, random.randint(1, 10)))
    graph.add_edge(Edge(1, 2, random.randint(1, 10)))

    assert graph.del_edge(Edge(1, 4)) is True
    assert graph.has_edge(Edge(1, 4)) is False
    assert graph.has_edge(Edge(4, 1)) is False

    assert graph.del_edge(Edge(1, 2)) is True
    assert graph.has_edge(Edge(1, 2)) is False
    assert graph.has_edge(Edge(2, 1)) is False

    graph.add_edge(Edge(1, 4, random.randint(1, 10)))
    graph.add_edge(Edge(1, 2, random.randint(1, 10)))

    assert graph.del_edge(Edge(4, 1)) is True
    assert graph.has_edge(Edge(1, 4)) is False
    assert graph.has_edge(Edge(4, 1)) is False

    assert graph.del_edge(Edge(2, 1)) is True
    assert graph.has_edge(Edge(1, 2)) is False
    assert graph.has_edge(Edge(2, 1)) is False

    # directed graph
    graph = Graph(5, True)
    graph.add_edge(Edge(1, 4, random.randint(1, 10)))
    graph.add_edge(Edge(1, 2, random.randint(1, 10)))

    assert graph.del_edge(Edge(1, 4)) is True
    assert graph.has_edge(Edge(1, 4)) is False

    assert graph.del_edge(Edge(1, 2)) is True
    assert graph.has_edge(Edge(2, 1)) is False


def test_weight():
    # undirected graph
    graph = Graph(5)
    graph.add_edge(Edge(1, 4, 3))
    graph.add_edge(Edge(1, 2, 4))

    assert graph.weight(Edge(1, 4)) == 3
    assert graph.weight(Edge(4, 1)) == 3
    assert graph.weight(Edge(1, 2)) == 4
    assert graph.weight(Edge(2, 1)) == 4

    # directed graph
    graph = Graph(5, True)
    graph.add_edge(Edge(1, 4, 3))
    graph.add_edge(Edge(1, 2, 4))
    graph.add_edge(Edge(4, 1, 2))
    graph.add_edge(Edge(2, 1, 6))

    assert graph.weight(Edge(1, 4)) == 3
    assert graph.weight(Edge(4, 1)) == 2
    assert graph.weight(Edge(1, 2)) == 4
    assert graph.weight(Edge(2, 1)) == 6


def test_iter_nodes():
    graph = Graph(5)

    res_list = [0, 1, 2, 3, 4]
    iterator_list = []

    for node in graph.iter_nodes():
        iterator_list.append(node)

    assert iterator_list.__eq__(res_list)


def test_adj_nodes():
    graph = Graph(5)
    graph.add_edge(Edge(1, 4, 3))
    graph.add_edge(Edge(1, 2, 4))
    graph.add_edge(Edge(4, 3, 2))

    list_res = [2, 4]
    list_nodes = []
    for node in graph.iter_adjacent(1):
        list_nodes.append(node)

    list_nodes.sort()
    assert list_nodes.__eq__(list_res)


def test_edges():
    # undirected graph
    graph1 = Graph(5)
    graph1.add_edge(Edge(1, 4, 3))
    graph1.add_edge(Edge(1, 2, 4))

    list_res = [Edge(1, 4, 3), Edge(4, 1, 3), Edge(1, 2, 4), Edge(2, 1, 4)]
    list_nodes = []
    for node in graph1.iter_edges():
        list_nodes.append(node)

    list_nodes.sort()
    assert list_nodes.__eq__(list_res)

    # directed graph
    graph1 = Graph(5, True)
    graph1.add_edge(Edge(1, 4, 3))
    graph1.add_edge(Edge(1, 2, 4))

    list_res = [Edge(1, 4, 3), Edge(1, 2, 4)]
    list_nodes = []
    for node in graph1.iter_edges():
        list_nodes.append(node)

    list_nodes.sort()
    assert list_nodes.__eq__(list_res)


def test_out_edges():
    graph = Graph(5)
    graph.add_edge(Edge(1, 4, 3))
    graph.add_edge(Edge(1, 2, 4))
    graph.add_edge(Edge(3, 1, 4))

    list_res = [Edge(1, 4, 3), Edge(1, 2, 4), Edge(1, 3, 4)]
    list_nodes = []
    for node in graph.iter_out_edges(1):
        list_nodes.append(node)

    list_nodes.sort()
    assert list_nodes.__eq__(list_res)


def test_in_edges():
    graph = Graph(5)
    graph.add_edge(Edge(1, 4, 3))
    graph.add_edge(Edge(1, 2, 4))
    graph.add_edge(Edge(3, 1, 4))

    list_res = [Edge(4, 1, 3), Edge(2, 1, 4), Edge(3, 1, 4)]
    list_nodes = []
    for node in graph.iter_in_edges(1):
        list_nodes.append(node)

    list_nodes.sort()
    assert list_nodes.__eq__(list_res)


def test_copy():
    assert Graph(4).copy().__eq__(Graph(4))
    assert Graph(1, True).copy().__eq__(Graph(1, True))

    # undirected graph
    graph1 = Graph(5)
    graph1.add_edge(Edge(1, 4, 3))
    graph1.add_edge(Edge(1, 2, 4))

    graph2 = Graph(5)
    graph2.add_edge(Edge(4, 1, 3))
    graph2.add_edge(Edge(2, 1, 4))

    assert graph1.copy().__eq__(graph2)
    assert graph2.copy().__eq__(graph1)

    # directed graph
    graph1 = Graph(5, True)
    graph1.add_edge(Edge(1, 4, 3))
    graph1.add_edge(Edge(1, 2, 4))

    graph2 = Graph(5, True)
    graph2.add_edge(Edge(1, 4, 3))
    graph2.add_edge(Edge(1, 2, 4))

    graph3 = Graph(5, True)
    graph3.add_edge(Edge(4, 1, 3))
    graph3.add_edge(Edge(2, 1, 4))

    assert graph1.copy().__eq__(graph2)
    assert graph1.copy().__ne__(graph3)


def test_transpose():
    assert Graph(4).transpose().__eq__(Graph(4))
    assert Graph(1, True).transpose().__eq__(Graph(1, True))

    # undirected graph
    graph1 = Graph(5)
    graph1.add_edge(Edge(1, 4, 3))
    graph1.add_edge(Edge(1, 2, 4))

    graph2 = Graph(5)
    graph2.add_edge(Edge(1, 4, 3))
    graph2.add_edge(Edge(1, 2, 4))

    assert graph1.transpose().__eq__(graph2)
    assert graph2.transpose().__eq__(graph1)

    # directed graph
    graph1 = Graph(5, True)
    graph1.add_edge(Edge(1, 4, 3))
    graph1.add_edge(Edge(1, 2, 4))

    graph2 = Graph(5, True)
    graph2.add_edge(Edge(1, 4, 3))
    graph2.add_edge(Edge(1, 2, 4))

    assert graph1.transpose().__ne__(graph2)


def test_complement():
    g1 = Graph(3)
    g1.add_edge(Edge(0, 1))
    g1.add_edge(Edge(0, 2))
    g1.add_edge(Edge(1, 2))

    print(g1.__repr__())
    print(Graph(3).complement().__repr__())

    assert g1.complement().__eq__(Graph(3))


def test_subgraph():
    g = Graph(4)
    g.add_edge(Edge(3, 1))
    g.add_edge(Edge(1, 2))
    g.add_edge(Edge(2, 0))
    g.add_edge(Edge(2, 3))
    assert g.has_edge(Edge(1, 3)) is True
    assert g.has_edge(Edge(1, 2)) is True
    assert g.has_edge(Edge(0, 2)) is True
    assert g.has_edge(Edge(2, 3)) is True

    subgraph = g.subgraph([0, 1])
    assert subgraph.has_edge(Edge(1, 3)) is False
    assert subgraph.has_edge(Edge(1, 2)) is False
    assert subgraph.has_edge(Edge(0, 2)) is False
    assert subgraph.has_edge(Edge(2, 3)) is True


if __name__ == '__main__':
    pytest.main()
