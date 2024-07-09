#include <bits/stdc++.h>

using namespace std;


int visited[25000] = {0};

void print_vec_2d(vector<vector<int>> &arr){
    printf("===========\n");
    for(int i = 0; i < arr.size(); i++){
        printf("%d %d\n", arr[i][0], arr[i][1]);
    }
}

int check(vector<vector<int>> &arr, int dist){
    memset(visited, 0, 25000*sizeof(visited[0]));
    //DFS
    vector<int> stack = {0};
    int count = 1;
    visited[0] = 1;
    while(stack.size()){
        int i = stack.back(); 
        stack.pop_back();
        int x1 =  arr[i][0]; 
        int y1 = arr[i][1];
        for(int j = 0; j < arr.size(); j++){
            int x2 =  arr[j][0]; 
            int y2 = arr[j][1];
            if(!visited[j] && dist >= pow((x1-x2), 2) + pow((y1-y2), 2)){
                visited[j] = 1;
                count += 1;
                stack.push_back(j);
            }

        }
    }
    if (arr.size() == count){
        return 1;
    }
    return 0;


}

int main(){
    freopen("moocast.in", "r", stdin);
    freopen("moocast.out", "w", stdout);
    int n;
    vector<vector<int>> arr;
    scanf("%d", &n);    
    for(int i = 0; i < n; i++){
        int x, y;
        scanf("%d %d", &x, &y);
        arr.push_back({x, y});
    }
    // print_vec_2d(arr);
    // bs
    int hi = 25000*25000;
    int lo = 0;
    while(lo < hi){
        int mid = (hi+lo)/2;
        if (check(arr, mid)){
            hi = mid;
        }
        else{
            lo = mid + 1;
        }
    }
    printf("%d\n", hi);
    return 0;

}