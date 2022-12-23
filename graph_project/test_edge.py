import pytest
from graph_project.edge import Edge


def test_repr():
    assert Edge(1, 2).__str__() == "Edge(1, 2)"
    assert Edge(1, 2, 4).__str__() == "Edge(1, 2, 4)"


def test_eq():
    assert Edge(1, 2).__eq__(Edge(1, 2)) is True
    assert Edge(2, 3, 4).__eq__(Edge(2, 3, 4)) is True


def test_ne():
    assert Edge(1, 2).__ne__(Edge(1, 4)) is True
    assert Edge(2, 3, 4).__ne__(Edge(1, 3, 4)) is True
    assert Edge(2, 3, 4).__ne__(Edge(2, 3)) is True


def test_lt():
    assert Edge(1, 2).__lt__(Edge(1, 4)) is True
    assert Edge(1, 2, 4).__lt__(Edge(1, 2, 8)) is True


def test_le():
    assert Edge(1, 2).__le__(Edge(1, 4)) is True
    assert Edge(1, 2, 4).__le__(Edge(1, 2, 8)) is True
    assert Edge(1, 2).__le__(Edge(1, 2)) is True
    assert Edge(1, 2, 5).__le__(Edge(1, 2, 5)) is True


def test_hash():
    assert Edge(1, 2).__hash__() == Edge(1, 2).__hash__()
    assert Edge(1, 2, 5).__hash__() == Edge(1, 2, 5).__hash__()


def test_invert():
    assert Edge(1, 2).__invert__() == Edge(2, 1)
    assert Edge(1, 2, 5).__invert__() == Edge(2, 1, 5)


if __name__ == '__main__':
    pytest.main()
