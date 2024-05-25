#include <bits/stdc++.h>

using namespace std;

typedef int64_t ll;

int main(){
    ll n, m;
    scanf("%ld %ld", &n , &m);
    unordered_map<ll, vector<ll>> adj;
    vector<ll> visited;
    vector<ll> roads;

    for(ll i = 1; i < n+1; i++){
        visited.push_back(0);
    }

    for(ll i = 0 ; i < m; i++){
        ll a, b;
        scanf("%ld %ld", &a, &b);
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    

    for(ll i = 1; i < n+1; i++){
        if (visited[i] == 0){
            roads.push_back(i);
            //DFS
            vector<ll> stack;
            stack.push_back(i);
            while (stack.size()){
                ll node = stack.back();
                stack.pop_back();
                for(ll j = 0; j < adj[node].size(); j++){
                    if (visited[adj[node][j]] == 0){
                    stack.push_back(adj[node][j]);
                    }
                }
                visited[node] = 1;
            }
        }
    }
    printf("%ld\n", roads.size() - 1);
    for(ll i = 0; i < roads.size() - 1; i++){
        printf("%ld %ld\n", roads[i], roads[i+1]);
    }

    return 0;
}

