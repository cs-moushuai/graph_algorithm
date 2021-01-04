#include <iostream>
#include <array>

using namespace std;

int main(void)
{
    array<array<int, 4>, 4> arr = {{{1, 3, 5, 7}, {2, 3, 4, 5}}};
    for (auto i : arr)
    {
        cout << i[0] << " ";
    }
    cout << endl;
    int visited_and_distance[7][2] = {{0, 0}};
    for (int i = 1; i < 7; ++i)
    {
        visited_and_distance[i][0] = 0;
        visited_and_distance[i][1] = 999;

    }
    cout << 1 << endl;
    printf("1\n");
    for (;;)
        ;

    return 0;
}
