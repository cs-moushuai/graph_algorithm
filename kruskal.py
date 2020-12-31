#!/usr/bin/env python3


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def root(self, parent, i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def unite(self, parent, rank, i, j):
        i_root = self.root(parent, i)
        j_root = self.root(parent, j)

        if rank[i_root] < rank[j_root]:
            parent[i_root] = j_root
        else:
            parent[j_root] = i_root
            if rank[i_root] == rank[j_root]:
                rank[i_root] += rank[j_root]

    def kruskal_algo(self):
        result = []
        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        self.graph = sorted(self.graph, key=lambda item: item[2])

        i = no_edge = 0
        while no_edge < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            if self.root(parent, u) != self.root(parent, v):
                no_edge += 1
                self.unite(parent, rank, u, v)
                result.append([u, v, w])

        print("Edge |  Weight")
        for u, v, w in result:
            print(f"{u} - {v}: {w}")


g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)
g.kruskal_algo()
