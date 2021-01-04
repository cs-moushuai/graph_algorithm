#include <iostream>

using namespace std;

class Graph
{
private:
    const int V = 5;
    const int graph[5][5] =
    {
        { 0, 9, 75, 0, 0 },
        { 9, 0, 95, 19, 42 },
        { 75, 95, 0, 51, 66 },
        { 0, 19, 51, 0, 31 },
        { 0, 42, 66, 31, 0 }
    };
    const int INF = 9999999;
public:
    Graph() = default;

    void prim_algo()
    {
        bool selected[V] = {false};
        selected[0] = true;
        cout << "Edge   |  Weight" << endl;
        for (int no_edge = 0; no_edge < V - 1; ++no_edge)
        {
            int minium = INF, x = 0, y = 0;
            for (int i = 0; i < V; ++i)
            {
                if (selected[i])
                {
                    for (int j = 0; j < V; ++j)
                    {
                        if (!selected[j] && graph[i][j] && graph[i][j] < minium)
                        {
                            minium = graph[i][j];
                            x = i;
                            y = j;

                        }

                    }
                }

            }
            selected[y] = true;
            cout << x << " - " << y << ": " << minium << endl;

        }
    }

};

int main(void)
{
    Graph g;
    g.prim_algo();

    return 0;
}
