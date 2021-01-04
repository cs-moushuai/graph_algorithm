#!/usr/bin/env python3

class Graph:
    INF = 9999999

    def __init__(self):

        self.V = 7
        self.graph = [[0, 0, 1, 2, 0, 0, 0],
                      [0, 0, 2, 0, 0, 3, 0],
                      [1, 2, 0, 1, 3, 0, 0],
                      [2, 0, 1, 0, 0, 0, 1],
                      [0, 0, 3, 0, 0, 2, 0],
                      [0, 3, 0, 0, 2, 0, 1],
                      [0, 0, 0, 1, 0, 1, 0]]

    def to_be_visited(self, visited_and_distance):
        for i in range(self.V):
            v = -10
            for index in range(self.V):
                if visited_and_distance[index][0] == 0 and \
                        (v < 0 or visited_and_distance[index][1] < visited_and_distance[v][1]):
                    v = index
        return v

    def dijkstra_algo(self):
        visited_and_distance = [[0, 0]]
        for i in range(self.V - 1):
            visited_and_distance.append([0, self.INF])
        for i in range(self.V):
            to_visit = self.to_be_visited(visited_and_distance)
            for neighbour in range(self.V):
                edge_weight = self.graph[to_visit][neighbour]
                new_distance = visited_and_distance[to_visit][1] + edge_weight
                curr_distance = visited_and_distance[neighbour][1]
                judge = not visited_and_distance[neighbour][0] and self.graph[to_visit][neighbour]
                if judge and new_distance < curr_distance:
                    visited_and_distance[neighbour][1] = new_distance
            visited_and_distance[to_visit][0] = 1
        for i in range(self.V):
            print(
                f"the distance from {chr(ord('a') + i)}: {visited_and_distance[i][1]}")


g = Graph()
g.dijkstra_algo()
