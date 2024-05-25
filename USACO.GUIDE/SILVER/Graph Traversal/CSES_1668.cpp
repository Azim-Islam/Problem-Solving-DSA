#include <bits/stdc++.h>

using namespace std;

typedef int64_t ll;

int main(){
    ll n, m;
    scanf("%ld %ld", &n, &m);
    unordered_map<ll, vector<ll>> adj;
    vector<ll> visited;
    for(ll i=0; i < n+1; i++){
        visited.push_back(0);
    }

    for(ll i=0; i < m; i++ ){
        ll a, b;
        scanf("%ld %ld", &a, &b);
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    
    vector<ll> stack;
    bool imp = false;

    for(ll i = 1; i < n+1; i++){
        if (!visited[i]){
            stack.push_back(i);
            visited[i] = 1;
            while(stack.size()){
                ll node = stack.back();
                stack.pop_back();
                for(ll j = 0; j < adj[node].size(); j++){
                    if (!visited[adj[node][j]]){
                        if (visited[node] == 1){
                            visited[adj[node][j]] = 2;
                        }
                        else{
                            visited[adj[node][j]] = 1;
                        }
                        stack.push_back(adj[node][j]);
                    }
                    else if (visited[node] == visited[adj[node][j]]){
                        imp = true;
                        }
                }

            }   
        }
        
        
    }
    if (imp){
        printf("IMPOSSIBLE\n");
    }
    else{
        for(int i = 1; i < n+1; i++){
            printf("%ld ", visited[i]);
        }
        printf("\n");
    }



    
    return 0;   
}