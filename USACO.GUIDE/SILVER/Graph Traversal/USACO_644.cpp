#pragma GCC target ("avx2")
#pragma GCC optimization ("O3")
#pragma GCC optimization ("unroll-loops")

#include <bits/stdc++.h>

using namespace std;

typedef int64_t ll;

bool FC(unordered_map<ll, vector<ll>> &adj, vector<ll> &closed, ll n)
{   
    vector<ll> visited;
    for (int i = 0; i < n+1; i++)
    {
        visited.push_back(0);
    }
    // dfs
    vector<ll> stack;
    ll start = 1;
    for(start=1; start < n+1; start++){
        if(!closed[start]){
            break;
        }
    }
    stack.push_back(start);
    visited[start] = 1;
    
    while (stack.size())
    {   
        ll node = stack.back();
        stack.pop_back();
        for (int i = 0; i < adj[node].size(); i++)
        {
            if (!visited[adj[node][i]] && !closed[adj[node][i]])
            {
                stack.push_back(adj[node][i]);
                visited[adj[node][i]] = 1;
            }
        }
    }
    for (int i = 1; i < n+1; i++)
    {
        if (visited[i] == 0 && closed[i] == 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    freopen("closing.in", "r", stdin);
    freopen("closing.out", "w", stdout);

    ll n, m;
    vector<ll> closed;
    unordered_map<ll, vector<ll>> adj;
    scanf("%ld %ld", &n, &m);
    for (int i = 0; i < n+1; i++)
    {
        closed.push_back(0);
    }

    for (int i = 0; i < m; i++)
    {
        ll a, b;
        scanf("%ld %ld", &a, &b);
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    if (FC(adj, closed, n))
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }
    for (int i = 1; i < n; i++)
    {
        ll a;
        scanf("%ld", &a);
        // adj.erase(a);
        closed[a] = 1;
        if (FC(adj, closed, n))
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }
    return 0;
}