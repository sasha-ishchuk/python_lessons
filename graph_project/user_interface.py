import sys
import time
from colorama import Fore, Style, Back

from graph_project.edge import Edge
from graph_project.file_utils import FileUtils
from graph_project.graph import Graph


class UserInterface:

    def __init__(self):
        pass

    @classmethod
    def start(cls):
        print(Fore.RED + Back.LIGHTGREEN_EX + "\033[1m HELLO! LET'S START OUR GRAPH JOURNEY!!! " + Style.RESET_ALL)
        cls.run_interface()

    @classmethod
    def run_interface(cls):
        print(Fore.GREEN + "\n1. Create graph \n2. Read graph from file")
        print(Style.RESET_ALL)
        answer = input("Choose option ['stop' to exit]: ")
        if answer == "1":
            cls.create_graph()
        elif answer == "2":
            cls.read_graph()
        elif answer == "stop":
            sys.exit()
        else:
            raise ValueError("Unrecognized answer!")

    @classmethod
    def read_graph(cls):
        print(Fore.GREEN + "\nChoose file you want to use: \n1. 'graph5.txt' \n2. 'graph10.txt' "
                           "\n3. 'graph6-directed.txt'")
        print(Style.RESET_ALL)
        answer = input("Choose option ['stop' to exit]: ")
        if answer == "1":
            print(Fore.LIGHTMAGENTA_EX + "\nCreating graph from 'graph5.txt' file...  result: ")
            print(Style.RESET_ALL)
            graph = FileUtils.read_graph_from_file("C:\\Users\\Sasha\\OneDrive\\Рабочий стол\\graph5.txt")
            print(graph.__repr__())
            time.sleep(2)
            cls.graph_manipulation(graph)
        elif answer == "2":
            print(Fore.LIGHTMAGENTA_EX + "\nCreating graph from 'graph10.txt' file...  result: ")
            print(Style.RESET_ALL)
            graph = FileUtils.read_graph_from_file("C:\\Users\\Sasha\\OneDrive\\Рабочий стол\\graph10.txt")
            print(graph.__repr__())
            time.sleep(2)
            cls.graph_manipulation(graph)
        elif answer == "3":
            print(Fore.LIGHTMAGENTA_EX + "\nCreating graph from 'result.txt' file...  result: ")
            print(Style.RESET_ALL)
            graph = FileUtils.read_graph_from_file("C:\\Users\\Sasha\\OneDrive\\Рабочий стол\\graph6-directed.txt")
            print(graph.__repr__())
            time.sleep(2)
            cls.graph_manipulation(graph)
        elif answer == "stop":
            sys.exit()
        else:
            raise ValueError("Unrecognized answer.")

    @classmethod
    def create_graph(cls):
        answer = input("\nChoose number of graph vertices ['stop' to exit]: ")
        if answer == "stop":
            sys.exit()
        try:
            answer = int(answer)
            print(Fore.LIGHTMAGENTA_EX + f"\nCreating graph with {answer} vertices...  result: ")
            print(Style.RESET_ALL)
            graph = Graph(answer)
            print(graph.__repr__())
            time.sleep(2)
            cls.graph_manipulation(graph)
        except ValueError:
            print("INT value required.")

    @classmethod
    def graph_manipulation(cls, graph):
        print(Fore.GREEN + "\nOPTIONS: \n0. Print graph \n1. Check vertices number \n2. Check edges number "
              + "\n3. Check graph is directed \n4. Check node exists \n5. Add edge \n6. Check edge exists "
              + "\n7. Delete edge \n8. Check edge's weight \n9. GO TO ITERATORS \n10. GO TO GRAPH'S TRANSFORMATION ")
        print(Style.RESET_ALL)

        answer = input("Choose option ['stop' to exit]: ")

        if answer == "stop":
            sys.exit()

        elif answer == "0":
            print(Fore.LIGHTMAGENTA_EX + "\nYour graph: \n" + graph.__repr__())
            print(Style.RESET_ALL)
            time.sleep(2)
            cls.graph_manipulation(graph)

        elif answer == "1":
            print(Fore.LIGHTMAGENTA_EX + f"\nNumber of graph vertices: {graph.v()}")
            print(Style.RESET_ALL)
            time.sleep(2)
            cls.graph_manipulation(graph)

        elif answer == "2":
            print(Fore.LIGHTMAGENTA_EX + f"\nNumber of graph edges: {graph.e()}")
            print(Style.RESET_ALL)
            time.sleep(2)
            cls.graph_manipulation(graph)

        elif answer == "3":
            print(Fore.LIGHTMAGENTA_EX + f"\nGraph is directed?: {graph.is_directed()}")
            print(Style.RESET_ALL)
            time.sleep(2)
            cls.graph_manipulation(graph)

        elif answer == "4":
            node = input("\nVertex number you want to check: ")
            try:
                node = int(node)
                print(Fore.LIGHTMAGENTA_EX + f"Does vertex exist?: {graph.has_node(node)}")
                print(Style.RESET_ALL)
                time.sleep(2)
                cls.graph_manipulation(graph)
            except ValueError:
                print("INT value required.")

        elif answer == "5":
            try:
                node1 = int(input("\nEdge source: "))
                node2 = int(input("Edge target: "))
                node3 = int(input("Edge weight: "))
                graph.add_edge(Edge(node1, node2, node3))
                print(Fore.LIGHTMAGENTA_EX + f"Does edge exist?: {graph.has_edge(Edge(node1, node2, node3))}")
                print(Style.RESET_ALL)
                time.sleep(2)
                cls.graph_manipulation(graph)
            except ValueError:
                print("INT value required.")

        elif answer == "6":
            try:
                node1 = int(input("\nEdge source: "))
                node2 = int(input("Edge target: "))
                node3 = int(input("Edge weight: "))
                print(Fore.LIGHTMAGENTA_EX + f"Does edge exist?: {graph.has_edge(Edge(node1, node2, node3))}")
                print(Style.RESET_ALL)
                time.sleep(2)
                cls.graph_manipulation(graph)
            except ValueError:
                print("INT value required.")

        elif answer == "7":
            try:
                node1 = int(input("\nEdge source: "))
                node2 = int(input("Edge target: "))
                node3 = int(input("Edge weight: "))
                graph.del_edge(Edge(node1, node2))
                print(Fore.LIGHTMAGENTA_EX + f"Does edge exist?: {graph.has_edge(Edge(node1, node2, node3))}")
                print(Style.RESET_ALL)
                time.sleep(2)
                cls.graph_manipulation(graph)
            except ValueError:
                print("INT value required.")

        elif answer == "8":
            try:
                node1 = int(input("\nEdge source: "))
                node2 = int(input("Edge target: "))
                print(Fore.LIGHTMAGENTA_EX + f"Edge weight: {graph.weight(Edge(node1, node2))}")
                print(Style.RESET_ALL)
                time.sleep(2)
                cls.graph_manipulation(graph)
            except ValueError:
                print("INT value required.")

        elif answer == "9":
            cls.graph_iterators(graph)

        elif answer == "10":
            cls.graph_transformations(graph)

        else:
            raise ValueError("Unrecognized answer.")

    @classmethod
    def graph_iterators(cls, graph):
        print(Fore.GREEN + "\nOPTIONS: \n0. BACK TO MAIN MENU \n1. Iterate over vertices "
              + "\n2. Iterate over adjacency vertices \n3. Iterate over edges \n4. Iterate over outgoing edges "
              + "\n5. Iterate over incoming edges ")
        print(Style.RESET_ALL)

        answer = input("Choose option ['stop' to exit]: ")

        if answer == "stop":
            sys.exit()

        elif answer == "0":
            time.sleep(2)
            cls.graph_manipulation(graph)

        elif answer == "1":
            print(Fore.LIGHTMAGENTA_EX + "\nLet's iterate over the graph vertices...")
            for i in graph.iter_nodes():
                print(i, end=" ")
            print(Style.RESET_ALL)
            time.sleep(2)
            cls.graph_iterators(graph)

        elif answer == "2":
            print(Fore.LIGHTMAGENTA_EX + "\nLet's iterate over the graph adjacency vertices...")
            for i in graph.iter_adjacent():
                print(i, end=" ")
            print(Style.RESET_ALL)
            time.sleep(2)
            cls.graph_iterators(graph)

        elif answer == "3":
            print(Fore.LIGHTMAGENTA_EX + "\nLet's iterate over the graph edges...")
            for i in graph.iter_edges():
                print(i, end=" ")
            print(Style.RESET_ALL)
            time.sleep(2)
            cls.graph_iterators(graph)

        elif answer == "4":
            print(Fore.LIGHTMAGENTA_EX + "\nLet's iterate over the graph outgoing edges...")
            node = input("\nVertex number to start: ")
            try:
                node = int(node)
                for i in graph.iter_out_edges(node):
                    print(i, end=" ")
                print(Style.RESET_ALL)
                time.sleep(2)
                cls.graph_iterators(graph)
            except ValueError:
                print("INT value required.")

        elif answer == "5":
            print(Fore.LIGHTMAGENTA_EX + "\nLet's iterate over the graph incoming edges...")
            node = input("\nVertex number to start: ")
            try:
                node = int(node)
                for i in graph.iter_in_edges(node):
                    print(i, end=" ")
                print(Style.RESET_ALL)
                time.sleep(2)
                cls.graph_iterators(graph)
            except ValueError:
                print("INT value required.")

        else:
            raise ValueError("Unrecognized answer.")

    @classmethod
    def graph_transformations(cls, graph):
        print(Fore.GREEN + "\nOPTIONS:: \n0. BACK TO MAIN MENU \n1. Copy graph \n2. Create transposed graph "
              + "\n3. Create complement of the graph1 \n4. Create induced subgraph ")
        print(Style.RESET_ALL)

        answer = input("Choose option ['stop' to exit]: ")

        if answer == "stop":
            sys.exit()

        elif answer == "0":
            time.sleep(2)
            cls.graph_manipulation(graph)

        elif answer == "1":
            print(Fore.LIGHTMAGENTA_EX + "\nCopy of your graph: ")
            print(graph.copy().__repr__())
            print(Style.RESET_ALL)
            time.sleep(2)
            cls.graph_transformations(graph)

        elif answer == "2":
            print(Fore.LIGHTMAGENTA_EX + "\nYour transposed graph: ")
            print(graph.transpose().__repr__())
            time.sleep(2)
            cls.graph_iterators(graph)

        elif answer == "3":
            print(Fore.LIGHTMAGENTA_EX + "\nComplement of your graph: ")
            print(graph.complement().__repr__())
            print(Style.RESET_ALL)
            time.sleep(2)
            cls.graph_iterators(graph)

        elif answer == "4":
            print(Fore.LIGHTMAGENTA_EX + "\nLet's choose vertices you want to exclude from graph... ")
            exclusion = []
            try:
                n = int(input("Enter number of vertices to exclude: "))
                for i in range(0, n):
                    elements = int(input("Enter each vertex, use ENTER: "))
                    exclusion.append(elements)
                print("\nInduced subgraph of your graph: ")
                print(graph.subgraph(exclusion).__repr__())
                print(Style.RESET_ALL)
            except ValueError:
                print("INT value required.")

        else:
            raise ValueError("Unrecognized answer.")


if __name__ == "__main__":
    UserInterface.start()
