class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            del self.adj_list[vertex]
            for v in self.adj_list:
                self.adj_list[v] = [vtx for vtx in self.adj_list[v] if vtx != vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1] = [vtx for vtx in self.adj_list[vertex1] if vtx != vertex2]
            self.adj_list[vertex2] = [vtx for vtx in self.adj_list[vertex2] if vtx != vertex1]

    def display(self):
        for vertex in self.adj_list:
            print(vertex, "->", " -> ".join(str(v) for v in self.adj_list[vertex]))


# Usage example:
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")

graph.display()
# Output:
# A -> B -> D
# B -> A -> C
# C -> B -> D
# D -> C -> A

graph.remove_edge("C", "D")
graph.remove_vertex("B")

graph.display()
# Output:
# A -> D
# D -> A
