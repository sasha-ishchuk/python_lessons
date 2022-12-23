class Edge:
    """ Class for directed weighted edge. """

    def __init__(self, source, target, weight=1):
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        """ Returns text edge representation. """
        if self.weight == 1:
            return "Edge({}, {})".format(repr(self.source), repr(self.target))
        else:
            return "Edge({}, {}, {})".format(
                repr(self.source), repr(self.target), repr(self.weight))

    def __eq__(self, other):
        """ Compares two edges (e1 == e2). """
        return (self.source, self.target, self.weight) == (
            other.source, other.target, other.weight)

    def __ne__(self, other):
        """ Compares two edges (e1 != e2). """
        return not self == other

    def __lt__(self, other):
        """ Compares two edges (e1 < e2). """
        return (self.weight, self.source, self.target) < (
            other.weight, other.source, other.target)

    def __le__(self, other):
        """ Compares two edges (e1 <= e2). """
        return (self.weight, self.source, self.target) <= (
            other.weight, other.source, other.target)

    def __hash__(self):
        """ Returns the hash code of edge. """
        return hash((self.source, self.target, self.weight))

    def __invert__(self):
        """ Returns edge with the opposite direction (~edge). """
        return Edge(self.target, self.source, self.weight)
