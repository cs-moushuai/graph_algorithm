#!/usr/bin/env python3

class Graph:
    INF = 9999999

    def __init__(self):
        self.V = 4
        self.graph = [[0, 3, self.INF, 5],
                      [2, 0, self.INF, 4],
                      [self.INF, 1, 0, self.INF],
                      [self.INF, self.INF, 2, 0]]

    def floyd_warshall(self):
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    self.graph[i][j] = min(
                        self.graph[i][k] + self.graph[k][j], self.graph[i][j])
        for i in range(self.V):
            for j in range(self.V):
                if self.INF == self.graph[i][j]:
                    print("INF", end=' ')
                else:
                    print(self.graph[i][j], end=' ')
            print()


g = Graph()
g.floyd_warshall()
