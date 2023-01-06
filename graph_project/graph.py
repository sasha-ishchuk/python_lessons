from copy import copy
import collections

from graph_project.edge import Edge


class Graph:
    """ Class for wighted graph, directed or undirected. """

    def __init__(self, n=0, directed=False):
        if n < 0:
            raise ValueError('Provide n >= 0')
        self.n = n
        self.directed = directed
        self.matrix = []
        for _ in range(self.n):
            self.matrix.append([0 for _ in range(self.n)])

    def __repr__(self):
        """ Returns text graph representation. """
        return '\n'.join(['\t'.join([str(i) for i in j]) for j in self.matrix])

    def __eq__(self, other):
        if self.n == other.n and self.directed == other.directed and self.matrix.__eq__(other.matrix):
            return True
        return False

    def v(self):
        """ Returns the number of vertices. """
        return self.n

    def e(self):
        """ Returns the number of edges. """
        edges = 0
        for row in self.matrix:
            for j in row:
                if j == 0:
                    continue
                elif j != 0:
                    edges += 1
        if self.is_directed():
            return edges
        else:
            return edges // 2

    def is_directed(self):
        """ bool, is graph directed? """
        return self.directed

    def add_node(self, node):
        """ Add vertex. """
        if 0 <= node < self.n:
            return True
        else:
            return False

    def has_node(self, node):
        """ Check if graph has such vertex. """
        if 0 <= node < self.n:
            return True
        else:
            return False

    def del_node(self, node):
        """ Delete vertex. """
        if 0 >= node > self.n:
            raise ValueError('Graph has not such vertex')
        else:
            for i in range(self.v()):
                self.matrix[i][node] = 0
            for i in range(self.v()):
                self.matrix[node][i] = 0

    def add_edge(self, edge):
        """ Add edge. """
        source = edge.source
        target = edge.target
        weight = edge.weight
        if (0 >= source > self.n) or (0 >= target > self.n):
            raise ValueError('Graph has not such vertex')
        elif source == target:
            raise ValueError('Graph could not have looped edge')
        elif not self.has_edge(Edge(source, target)) and self.is_directed():
            self.matrix[source][target] = weight
        elif not self.has_edge(Edge(source, target)):
            self.matrix[source][target] = weight
            self.matrix[target][source] = weight

    def has_edge(self, edge):
        """ Check if graph has such edge. """
        source = edge.source
        target = edge.target
        if source < 0 or source > self.n or target < 0 or target > self.n:
            raise IndexError('Graph has not such vertices')
        else:
            if self.matrix[source][target] != 0:
                return True
            else:
                return False

    def del_edge(self, edge):
        """ Delete edge. """
        source = edge.source
        target = edge.target
        if (0 <= source < self.n) or (0 <= target < self.n):
            if self.directed:
                self.matrix[source][target] = 0
                return True
            elif not self.directed:
                self.matrix[source][target] = 0
                self.matrix[target][source] = 0
                return True
        else:
            raise ValueError('Graph has not such vertices or edge')

    def weight(self, edge):
        """ Returns edge's weight. """
        source = edge.source
        target = edge.target
        if source < 0 or source > self.n or target < 0 or target > self.n:
            raise IndexError('Graph has not such vertices')
        elif self.matrix[source][target] == 0:
            print('Graph has not such edge')
        else:
            return self.matrix[source][target]

    def iter_nodes(self):
        """ Iterate over the vertices. """
        return iter(range(self.n))

    def iter_adjacent(self, node):
        """ Iterate over the adjacency vertices. """
        for i in range(self.n):
            if self.matrix[node][i] != 0:
                yield i

    def iter_out_edges(self, node):
        """ Iterate over the outgoing edges. """
        for i in range(self.n):
            if self.matrix[node][i] != 0:
                source = node
                target = i
                weight = self.matrix[source][target]
                yield Edge(source, target, weight)

    def iter_in_edges(self, node):
        """ Iterate over the incoming edges. """
        for i in range(self.n):
            if self.has_edge(Edge(i, node)):
                source = i
                target = node
                weight = self.matrix[i][node]
                yield Edge(source, target, weight)

    def iter_edges(self):
        """ Iterate over edges. """
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] != 0:
                    if not self.directed:
                        yield Edge(i, j, self.matrix[i][j])
                    else:
                        if i < j:
                            yield Edge(i, j, self.matrix[i][j])

    def copy(self):
        """ Returns the copy of the graph. """
        copied_graph = Graph(self.n, self.directed)
        copied_graph.matrix = copy(self.matrix)
        return copied_graph

    def transpose(self):
        """ Returns a transposed graph. """
        transposed_graph = self.copy()
        for i in range(self.n):
            for j in range(self.n):
                transposed_graph.matrix[j][i] = self.matrix[i][j]
        return transposed_graph

    def complement(self):
        """ Returns the complement of the graph. """
        comp_graph = self.copy()
        for i in range(self.n):
            for j in range(self.n):
                if comp_graph.matrix[i][j] == 0 and i != j:
                    comp_graph.matrix[i][j] = 1
                elif comp_graph.matrix[i][j] != 0:
                    comp_graph.matrix[i][j] = 0
        return comp_graph

    def subgraph(self, nodes):
        """ Returns the induced subgraph. """
        subgraph = self.copy()
        for i in nodes:
            subgraph.del_node(i)
        return subgraph

    def dfs_util(self, start, visited):

        # Print current node
        print(start, end=' ')

        # Set current node as visited
        visited[start] = True

        # For every node of the graph
        for i in range(self.n):
            if self.matrix[start][i] != 0 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start):
        visited = [False] * self.n
        self.dfs_util(start, visited)

    def bfs(self, start):
        visited = [False] * self.n
        q = collections.deque([start])

        # Set current node as visited
        visited[start] = True

        while q:
            vis = q[0]
            # Print current node
            print(vis, end=' ')
            q.popleft()

            for i in range(self.n):
                if self.matrix[vis][i] != 0 and not visited[i]:
                    q.append(i)
                    visited[i] = True
