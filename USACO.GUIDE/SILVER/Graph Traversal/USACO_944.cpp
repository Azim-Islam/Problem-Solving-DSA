#include <bits/stdc++.h>

using namespace std;

typedef int64_t ll;

struct cow{
    int number;
    int x;
    int y;
};

bool check(unordered_map<int, cow> &cows, unordered_map<int, vector<int>> &adj, int n, int peri){
    //DFS
    unordered_map<int, bool> visited;
    for(int i = 1; i < n+1; i++){
        visited[i] = false;
    }
    int min_peri = 1e9;
    for(int i = 1; i < n+1; i++){
        
        if(!visited[i]){
            int max_x = -1, max_y = -1;
            int min_x = 1e9, min_y = 1e9;

            vector<cow> stack;
            stack.push_back(cows[i]);
            visited[i] = true;

            while(stack.size()){
                cow node = stack.back();
                min_x = min(min_x, node.x);
                max_x = max(max_x, node.x);
                max_y = max(max_y, node.y);
                min_y = min(min_y, node.y);
                stack.pop_back();
                for(auto c: adj[node.number]){
                    if(!visited[c]){
                        stack.push_back(cows[c]);
                        visited[c] = true;
                    }
                }
            }
            min_peri = min(min_peri, 2*abs(max_x-min_x) + 2*abs(min_y-max_y));
            // printf("min perimeter from %d is = %d\n", i, min_peri);
        }
        
    }
    if(min_peri <= peri){
        return true;
    }
    return false;
}

int main(){
    freopen("fenceplan.in", "r", stdin);
    freopen("fenceplan.out", "w", stdout);

    int n, m;
    unordered_map<int, vector<int>> adj;
    unordered_map<int, cow> cows;

    
    scanf("%d %d", &n, &m);

    for(int i = 0; i<n; i++){
        cow a;
        a.number = i+1;
        scanf("%d %d", &a.x, &a.y);
        cows[i+1] = a;
    }

    for(int i = 0; i<m ; i++){
        int a, b;
        scanf("%d %d", &a, &b);
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    int hi = 1e9;
    int lo = 0;

    while(lo < hi){
        int mid = (hi+lo)/2;
        if (check(cows, adj, n, mid)){
            hi = mid;
        }
        else{
            lo = mid + 1;
        }
    }
    printf("%d\n", hi);

    
}