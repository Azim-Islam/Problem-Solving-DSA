#include <bits/stdc++.h>

using namespace std;
int adj[21][21] = {0};
int ans[21] = {0};

int main(){
    int N, K;
    scanf("%d %d", &N, &K);
    for(int i = 0; i < K; i++){
        int a, b, s_a, s_b;
        scanf("%d %d %d %d", &a, &b, &s_a, &s_b);
        if(s_a > s_b){
            adj[a][b] = 1;
        }
        else{
            adj[b][a] = 1;
        }
    }
    
    for(int i = 1; i<=N; i++){
        //dfs
        vector<int> stack;
        unordered_map<int, bool> visited;
        stack.push_back(i);
        visited[i] = true;
        while(stack.size()){
            int node = stack.back();
            stack.pop_back();
            for(int j = 1; j <= N; j++){
                if (adj[node][j] && j == i){
                    ans[i] = 1;
                }
                else if (adj[node][j] && !visited[j]){
                    stack.push_back(j); 
                    visited[j] = true; 
                }
            }
        }
    }
    printf("%d\n", accumulate(begin(ans), end(ans), 0));    
}

