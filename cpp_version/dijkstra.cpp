#include <iostream>
#include <cstdio>
#include <array>

using namespace std;

class Graph
{
private:
    const int INF;
    const int V;
    const array<array<int, 7>, 7> graph;
public:
    Graph(): INF(99999), V(7)
        , graph{{

            {0, 0, 1, 2, 0, 0, 0},
            {0, 0, 2, 0, 0, 3, 0},
            {1, 2, 0, 1, 3, 0, 0},
            {2, 0, 1, 0, 0, 0, 1},
            {0, 0, 3, 0, 0, 2, 0},
            {0, 3, 0, 0, 2, 0, 1},
            {0, 0, 0, 1, 0, 1, 0}

        }}
    {}
    int to_be_visited(int visited_and_distance[][2])
    {
        int v = 0;
        for (int i = 0; i < V; i++)
        {
            v = -10;
            for (int index = 0; index < V; index++)
            {
                if (visited_and_distance[index][0] == 0 &&
                        (v < 0 || visited_and_distance[index][1] < visited_and_distance[v][1]))
                {
                    v = index;
                }
            }
        }
        return v;
    }

    void dijkstra_algo()
    {
        int visited_and_distance[7][2] = {{0, 0}};
        for (int i = 1; i < V; ++i)
        {
            visited_and_distance[i][0] = 0;
            visited_and_distance[i][1] = INF;

        }
        for (int i = 0; i < V; ++i)
        {
            int to_visit = to_be_visited(visited_and_distance);
            for (int neighbour = 0; neighbour < V; neighbour++)
            {
                int edge_weight = graph[to_visit][neighbour];
                int new_distance = visited_and_distance[to_visit][1] + edge_weight;
                int curr_distance = visited_and_distance[neighbour][1];
                int judge = !visited_and_distance[neighbour][0] && graph[to_visit][neighbour];
                if (judge && new_distance < curr_distance)
                {
                    visited_and_distance[neighbour][1] = new_distance;
                }

            }
            visited_and_distance[to_visit][0] = 1;

        }
        for (int i = 0; i < V; i++)
        {
            cout << "the distance from " << char('a' + i) << ": " << visited_and_distance[i][1] << endl;
        }


    }
};

int main(void)
{
    Graph graph;
    graph.dijkstra_algo();


    return 0;
}
