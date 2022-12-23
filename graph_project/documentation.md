Class for a weighted graph, directed or undirected.

Attributes:
    n (int): The number of vertices in the graph.
    directed (bool): Is the graph directed or not. Default value is False.
    matrix (List[List[int]]): A 2D matrix representing the graph.

Methods:
    
__init__(self, n=0, directed=False):
        Initializes the graph with a given number of vertices and a flag indicating whether the graph is directed.
    
__repr__(self):
        Returns a string representation of the graph.

__eq__(self, other):
        Compares two graphs for equality.
        Returns:
            bool: True if the graphs are equal, False otherwise.

v(self):
        Returns the number of vertices in the graph.
    
e(self):
        Returns the number of edges in the graph.
    
is_directed(self):
        Returns a boolean indicating whether the graph is directed.
    
add_node(self, node):
        Adds a vertex to the graph.
    
has_node(self, node):
        Returns a boolean indicating whether the graph has a given vertex.
    
del_node(self, node):
        Deletes a vertex from the graph.
    
add_edge(self, edge):
        Adds an edge to the graph.
    
has_edge(self, edge):
        Returns a boolean indicating whether the graph has a given edge.
    
del_edge(self, edge):
        Deletes an edge from the graph.
    
weight(self, edge):
        Returns the weight of a given edge.
    
iter_nodes(self):
        Returns a list of the vertices in the graph.
    
iter_edges(self):
        Returns a list of the edges in the graph.
    
iter_out_edges(self, node):
        Returns a list of the edges outgoing from a given vertex.
    
iter_in_edges(self, node):
        Returns a list of the edges incoming to a given vertex.

copy(self):
        Returns a copy of the graph.
        
transpose(self):
        Returns a transposed version of the graph.
        
complement(self):
        Returns the complement of the graph.
        
subgraph(self, nodes):
        Returns the induced subgraph of the graph. 
        nodes (list): A list of vertices to exclude from the subgraph.
            
dfs_util(self, start, visited):
        A helper function for the dfs() method that performs the depth-first search on the graph.
            start (int): The starting vertex for the search.
            visited (list): A list of booleans indicating whether each vertex has been visited.
            
dfs(self, start):
        Perform a depth-first search on the graph, starting at the given vertex.
            start (int): The starting vertex for the search.
            
bfs(self, start):
        Perform a breadth-first search on the graph, starting at the given vertex.
            start (int): The starting vertex for the search.


____
#### A utility class for reading and writing graphs to and from files.

Attributes:
    None

Methods:
__init__(self):
        Initializes the FileUtils object.
        
read_graph_from_file(path):
        Reads a graph from a file at the given path.
            path (str): The path to the file.
        Returns:
            graph (Graph): A graph object representing the graph in the file.
            
write_graph_to_file(graph, path):
        Writes a graph to a file at the given path.
            graph (Graph): The graph to write to the file.
            path (str): The path to the file.

____
#### A class for directed weighted edges.

Attributes:
    source (int): The source vertex of the edge.
    target (int): The target vertex of the edge.
    weight (int): The weight of the edge. Default value is 1.

Methods:

__init__(self, source, target, weight=1):
        Initializes the Edge object.
            source (int): The source vertex of the edge.
            target (int): The target vertex of the edge.
            weight (int): The weight of the edge. Default value is 1.
            
__repr__(self):
        Returns a string representation of the edge.
            
__eq__(self, other):
        Compares two edges for equality (e1 == e2).
        Returns:
            bool: True if the edges are equal, False otherwise.
            
__ne__(self, other):
        Compares two edges for inequality (e1 != e2).
        Returns:
            bool: True if the edges are not equal, False otherwise.
            
__lt__(self, other):
        Compares two edges for ordering (e1 < e2).
        Returns:
            bool: True if the first edge is less than the second edge, False otherwise.
            
__le__(self, other):
        Compares two edges for ordering (e1 <= e2).
        Returns:
            bool: True if the first edge is less than or equal to the second edge, False otherwise.
            
__hash__(self):
        Returns the hash code of the edge.
        
__invert__(self):
        Returns an edge with the opposite direction (~edge).
