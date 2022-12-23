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
    pass


def test_has_node():
    assert Graph(5).has_node(4) is True
    assert Graph(5).has_node(5) is False


def test_del_node():
    pass


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
    iterator = ""

    for node in graph.iter_nodes():
        iterator += str(node)

    assert " ".join(iterator) == "0 1 2 3 4"


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

    graph3 = Graph(5, True)
    graph3.add_edge(Edge(4, 1, 3))
    graph3.add_edge(Edge(2, 1, 4))

    assert graph1.transpose().__ne__(graph2)
    assert graph1.transpose().__eq__(graph3)


def test_complement():
    assert Graph(4).complement().__eq__(Graph(4))
    assert Graph(1, True).complement().__eq__(Graph(1, True))

    # undirected graph
    graph1 = Graph(3)
    graph1.add_edge(Edge(1, 2))
    graph1.add_edge(Edge(0, 2))

    graph2 = Graph(3)
    graph2.add_edge(Edge(1, 0))

    assert graph1.complement().__eq__(graph2)
    assert graph2.complement().__eq__(graph1)

    # undirected graph
    graph1 = Graph(3, True)
    graph1.add_edge(Edge(1, 2))
    graph1.add_edge(Edge(0, 2))
    graph1.add_edge(Edge(2, 1))
    graph1.add_edge(Edge(0, 1))

    graph2 = Graph(3)
    graph2.add_edge(Edge(2, 0))
    graph2.add_edge(Edge(1, 0))

    assert graph1.complement().__eq__(graph2)
    assert graph2.complement().__eq__(graph1)


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
