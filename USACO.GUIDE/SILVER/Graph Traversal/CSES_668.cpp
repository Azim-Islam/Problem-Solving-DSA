#include <bits/stdc++.h>
using namespace std;
typedef int64_t ll;

struct Node
{
    int x;
    int y;
    int p;
};

bool distance(Node point, Node other)
{
    if (sqrt(pow(point.x - other.x, 2) + pow(point.y - other.y, 2)) <= point.p)
    {
        // printf("distance false {%d}\n", point.p);
        return true;
    }
    // printf("distance true {%d}\n", point.p);

    return false;
}

bool not_visited(vector<Node> &visited, Node point)
{
    for (auto node : visited)
    {
        if (node.x == point.x && node.y == point.y && node.p == point.p)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    freopen("moocast.in", "r", stdin);
    freopen("moocast.out", "w", stdout);
    int n, ans = 0;
    vector<Node> arr;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        Node point;
        scanf("%d %d %d", &point.x, &point.y, &point.p);
        arr.push_back(point);
    }

    ans = 0;
    for (int i = 0; i < n; i++)
    {
        vector<Node> visited;
        vector<Node> stack;

        stack.push_back(arr[i]);
        visited.push_back(arr[i]);

        while ((int)stack.size() != 0)
        {
            Node point = stack.back();
            stack.pop_back();
            for (int j = 0; j < n; j++)
            {
                if (distance(point, arr[j]) && not_visited(visited, arr[j]) && i != j)
                {
                    stack.push_back(arr[j]);
                    visited.push_back(arr[j]);

                    // printf("Found one %d visited size {%d} for {%d}\n", arr[j].p, visited.size(), point.p);
                }
            }
        }
        ans = max(ans, (int)visited.size());
    }
    printf("%d\n", ans);

    return 0;
}