Design an application for a thermal power station and electrical lines that are connected among various power stations. 
The costs of electrification involved appear as weights on the edges. 
Obtain the minimum possible connection among the thermal stations so that any two thermal stations can be linked with the minimum cost involved.
import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def print_mst(self, parent):
        print("Thermal Station   --   Connected to   -->   Thermal Station   Cost")
        for i in range(1, self.V):
            print(f"   {i}                   --                  {parent[i]}                   {self.graph[i][parent[i]]}")

    def prim_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        parent[0] = -1

        for _ in range(self.V):
            min_key = sys.maxsize
            min_index = 0

            for v in range(self.V):
                if key[v] < min_key and not mst_set[v]:
                    min_key = key[v]
                    min_index = v

            mst_set[min_index] = True

            for v in range(self.V):
                if self.graph[min_index][v] > 0 and not mst_set[v] and self.graph[min_index][v] < key[v]:
                    key[v] = self.graph[min_index][v]
                    parent[v] = min_index

        self.print_mst(parent)

# Accepting user input
n = int(input("Enter the number of thermal power stations: "))+
g = Graph(n)

print("Enter the cost of electrification for each connection:")
for i in range(n):
    for j in range(i+1, n):
        cost = int(input(f"Enter the cost between thermal station {i} and {j}: "))
        g.add_edge(i, j, cost)
g.prim_mst()
