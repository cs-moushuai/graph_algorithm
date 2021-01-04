#include <iostream>

using namespace std;

class Graph
{
private:
    const int INF = 9999999;
    const int V = 4;
    int graph[4][4] =
    {
        {0, 3, INF, 5},
        {2, 0, INF, 4},
        {INF, 1, 0, INF},
        {INF, INF, 2, 0}
    };

public:
    void PrintGraph()
    {
        for (int i = 0; i < V; ++i)
        {
            for (int j = 0; j < V; ++j)
            {
                if (graph[i][j] == INF)
                {
                    cout << "INF" << " ";
                }
                else
                {
                    cout << graph[i][j] << " ";
                }

            }
            cout << endl;

        }

    }
    void floyd_warshall_algo()
    {
        for (int k = 0; k < V; ++k)
        {
            for (int i = 0; i < V; ++i)
            {
                for (int j = 0; j < V; ++j)
                {
                    graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j]);

                }

            }

        }
        PrintGraph();

    }




};

int main(void)
{
    Graph g;
    g.floyd_warshall_algo();

    return 0;
}
