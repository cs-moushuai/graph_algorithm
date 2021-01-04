#!/usr/bin/env python3


class Graph:
    INF = 9999999

    def __init__(self):
        self.V = 5
        self.G = [[0, 9, 75, 0, 0],
                  [9, 0, 95, 19, 42],
                  [75, 95, 0, 51, 66],
                  [0, 19, 51, 0, 31],
                  [0, 42, 66, 31, 0]]

    def prim_algo(self):
        selected = [False] * 5
        selected[0] = True
        print("Edge |  Weight")
        for no_edge in range(self.V - 1):
            minium = self.INF
            x, y = 0, 0
            for i in range(self.V):
                if selected[i]:
                    for j in range(self.V):
                        if not selected[j]:
                            if self.G[i][j] and minium > self.G[i][j]:
                                minium = self.G[i][j]
                                x, y = i, j
            selected[y] = True
            print(f"{x} - {y}:  {minium:<4}")


g = Graph()
g.prim_algo()
