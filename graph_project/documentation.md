# *graph_project*

***Final project for Python classes, UJ***

For ADT of lecture graphs created graph implementation based on 
adjacency matrix (list of lists). Vertices are int numbers 
from 0 to n-1. Implemented BFS and DFS.

---
### Table of contents:
1. [Classes](#1-classes)
2. [Tests](#2-tests)

___
# 1. Classes

## Graph (*graph.py*)
#### *Class for a weighted graph, directed or undirected.*

### Attributes:
* ```n (int):``` the number of vertices in the graph.
* ```directed (bool):``` is the graph directed or not. Default value *False*.
* ```matrix (List[List[int]]):``` 2D matrix representing the graph.

### Methods:
    
1. ```__init__ (self, n=0, directed=False):``` initializes the graph 
with a given number of vertices and a flag indicating whether the graph is directed.

2. ```__repr__ (self):```
    - Parameters:
        - self: the class object.
    - Returns: 
        - **string**: text representation of the graph.

3. ```__eq__ (self, other):``` compares two graphs for equality.
    - Parameters:
        - self: the class object.
        - other: the class object.
    - Returns: 
        - **bool**: True if the graphs are equal, False otherwise.

4. ```v (self):```
    - Parameters:
        - self: the class object.
    - Returns: 
        - **int**: the number of vertices in the graph.

5. ```e (self):```
    - Parameters:
        - self: the class object.
    - Returns: 
        - **int**: the number of edges in the graph.
 
6. ```is_directed (self):```
    - Parameters:
        - self: the class object.
    - Returns: 
        - **bool**: True if the graph is directed, False otherwise.

7. ```add_node (self, node):``` adds a vertex to the graph.
    - Parameters:
        - self: the class object.
        - **node** (int): vertex number to add.
    - Returns: 
        - **bool**: True if the given vertex was added, False otherwise.

8. ```has_node (self, node):```
    - Parameters:
        - self: the class object.
        - **node** (int): vertex number to check if exists.
    - Returns: 
        - **bool**: True if the graph has a given vertex, False otherwise.

9. ```del_node (self, node):``` deletes a vertex from the graph.
    - Parameters:
        - self: the class object.
        - **node** (int): vertex number to delete.
    - Returns: None.
    
10. ```add_edge (self, edge):``` adds an edge to the graph.
    - Parameters:
        - self: the class object.
        - **edge** (Edge): edge to add.
    - Returns: None.

11. ```has_edge (self, edge):```
    - Parameters:
        - self: the class object.
        - **edge** (Edge): edge to check if exists.
    - Returns: 
        - **bool**: True if the graph has a given edge, False otherwise.

12. ```del_edge (self, edge):``` deletes an edge from the graph.
    - Parameters:
        - self: the class object.
        - **edge** (Edge): edge to delete.
    - Returns: None.

13. ```weight (self, edge):```
    - Parameters:
        - self: the class object.
        - **edge** (Edge): edge to get it weight.
    - Returns: 
        - **int**: the weight of a given edge.

14. ```iter_nodes (self):``` iterate over vertices in the graph.
    - Parameters:
        - self: the class object.
    - Returns: None.

15. ```iter_edges (self):``` iterate over edges in the graph.
    - Parameters:
        - self: the class object.
    - Returns: None.

16. ```iter_out_edges (self, node):``` iterate over edges outgoing from a given vertex.
    - Parameters:
        - self: the class object.
        - **node** (Edge): start edge to iterate.
    - Returns: None.

17. ```iter_in_edges (self, node):``` iterate over edges incoming to a given vertex.
    - Parameters:
        - self: the class object.
        - **node** (Edge): start edge to iterate.
    - Returns: None.

18. ```copy (self):```
    - Parameters:
        - self: the class object.
    - Returns: 
        - **Graph**: a copy of the graph.

19. ```transpose (self):```
    - Parameters:
        - self: the class object.
    - Returns: 
        - **Graph**: a transposed version of the graph.

20. ```complement (self):```
    - Parameters:
        - self: the class object.
    - Returns: 
        - **Graph**: the complement of the graph.

21. ```subgraph (self, nodes):```
    - Parameters:
        - self: the class object.
        - **nodes** (list): a list of vertices to exclude from the subgraph.
    - Returns: 
        - **Graph**: the induced subgraph of the graph. 

22. ```dfs_util (self, start, visited):``` a helper function for the ***dfs()*** method that performs the depth-first search on the graph.
    - Parameters:
        - self: the class object.
        - **start** (int): the starting vertex for the search.
        - **visited** (list): a list of booleans indicating whether each vertex has been visited.
    - Returns: None

23. ```dfs (self, start):``` perform a ***Depth First Search*** algorithm on the graph, starting at the given vertex.
    - Parameters:
        - self: the class object.
        - **start** (int): the starting vertex for the search.
24. Returns: None

25. ```bfs (self, start):``` perform a ***Breadth First Search*** algorithm on the graph, starting at the given vertex.
    - Parameters:
        - self: the class object.
        - **start** (int): the starting vertex for the search.
    - Returns: None


___
## Edge (*edge.py*)
#### *A class for directed weighted edge.*

### Attributes:
- ```source (int):``` the source vertex of the edge.
- ```target (int):``` the target vertex of the edge.
- ```weight (int):``` the weight of the edge. Default value is *1*.

### Methods:

1. ```__init__ (self, source, target, weight=1):``` 
initializes the Edge object with a given class attributes.

2. ```__repr__ (self):```
   - Parameters:
       - self: the class object.
   - Returns: 
       - **string**: text representation of the graph.

3. ```__eq__ (self, other):``` compares two edges for equality *(e1 == e2)*.
   - Parameters:
       - self: the class object. 
       - other: the class object.
   - Returns: 
       - **bool**: True if the graphs are equal, False otherwise.
 
4. ```__ne__ (self, other):``` compares two edges for inequality (e1 != e2).
   - Parameters:
       - self: the class object. 
       - other: the class object.
   - Returns: 
       - **bool**: True if the graphs are equal, False otherwise.
 
5. ```__lt__ (self, other):``` compares two edges for ordering (e1 < e2).
   - Parameters:
       - self: the class object. 
       - other: the class object.
   - Returns: 
       - **bool**: True if the first edge is less than the second edge, False otherwise.
  
6. ```__le__ (self, other):``` compares two edges for ordering (e1 <= e2).
   - Parameters:
       - self: the class object. 
       - other: the class object.
   - Returns: 
       - **bool**: True if the first edge is less than or equal to the second edge, False otherwise.

7. ```__hash__ (self): ```
   - Parameters:
       - self: the class object. 
   - Returns: 
       - **int**: the hash code of the edge.
 
8. ```__invert__ (self):```
   - Parameters:
       - self: the class object. 
   - Returns: 
       - **Edge**: an edge with the opposite direction (~edge).


___
## FileUtils (*file_utils.py*)
#### *A utility class for reading and writing graphs to and from files.*

### Attributes: 

- None

### Methods:
1. ```__init__ (self):``` *pass*.

2. ```read_graph_from_file (path): ```reads a graph from a file at the given path.
   - Parameters:
       - **path** (str): the path to the file.
   - Returns:
       - **Graph**: a graph object representing the graph in the file.

3. ```write_graph_to_file (graph, path):``` writes a graph to a file at the given path.
   - Parameters:
       - **graph** (Graph): the graph to write to the file.
       - **path** (str): the path to the file.
   - Returns: None


___
## UserInterface (user_interface.py)
#### *A class that provides a command-line interface for interacting with a graph.*
***It allows the user:***
- *create a new graph or read a graph from a file,* 
- *manipulate the graph by adding and deleting edges, checking if nodes or 
edges exist, and checking the number of vertices and edges,* 
- *iterate through the graph,* 
- *transform graph,*
- *use search algorithms.*

NOTE: *The user can exit the interface at any time by typing **'stop'**.*


### Attributes:
- None

### Methods:
    
1. ```__init__ (self): ``` *pass*

2. ```start (cls):``` starts the interface by printing a greeting 
message and calling the *run_interface* method.
   - Parameters:
       - cls: the class object. 
   - Returns: None

3. ```run_interface (cls):``` displays a menu of options to the user and calls the appropriate method based on the user's input.
   - Parameters:
       - cls: the class object. 
   - Returns: None

4. ```read_graph (cls):``` prompts the user to select a file, creates a graph using the *read_graph_from_file* method
from *FileUtils* class, and calls the *graph_manipulation* method.
   - Parameters:
       - cls: the class object. 
   - Returns: None

5. ```create_graph(cls):``` prompts the user to enter the number of vertices in the graph and whether the graph should be directed. 
It then creates a new graph using the *Graph()* constructor from *Graph* class.
   - Parameters:
       - cls: the class object. 
   - Returns: None

6. ```graph_manipulation(cls, graph):``` presents the user with a list of options for manipulating the graph. 
If the user types **'stop'**, it exits the interface.
   - Parameters:
       - cls: the class object.
       - graph (**Graph**): object representing the graph.
   - Returns: None

7. ```graph_iterators(cls, graph):``` presents the user with a list of options for iterate over the graph. 
If the user types **'0'** - it goes to previous menu, if **'stop'** - it exits the interface.
   - Parameters:
       - cls: the class object.
       - graph (**Graph**): object representing the graph.
   - Returns: None

8. ```graph_transformations(cls, graph):``` presents the user with a list of options to transform the graph
(copy graph, create its complement, subgraph or transposed version).
If the user types **'0'** - it goes to previous menu, if **'stop'** - it exits the interface.
   - Parameters:
       - cls: the class object.
       - graph (**Graph**): object representing the graph.
   - Returns: None

9. ```search_algorithms(cls, graph):``` presents the user with a list of options of search algorithms (DFS or BFS). 
If the user types **'0'** - it goes to previous menu, if **'stop'** - it exits the interface.
   - Parameters:
       - cls: the class object.
       - graph (**Graph**): object representing the graph.
   - Returns: None


___
# 2. Tests

### ***1. test_graph.py***
#### *This test file tests the implementation of the Graph class which represents directed or undirected graph.*

USE: pytest library.

### ***2. test_edge.py***
#### *This test file tests the implementation of the Edge class which represents an edge in a graph.*

USE: pytest library.
