#include <bits/stdc++.h>

using namespace std;

int check(vector<int> &arr, int k, int tmax){
    priority_queue<int, vector<int>, greater<int>> pq;
    int m= -1;
    for(int i=0; i<k; i++){
        m = max(m, arr[i]); 
        pq.push(arr[i]);
    }

    for(int i=k; i < arr.size(); i++){
        int v = pq.top();
        pq.pop();
        m = max(m, arr[i]+v);
        pq.push(arr[i]+v);
    }

    if (m > tmax){
        return 0;
    }

    else{
        return 1;
    }


}

int main(){
    int n, tmax;


    freopen("cowdance.in", "r", stdin);
    freopen("cowdance.out", "w", stdout);



    scanf("%d %d", &n, &tmax);
    vector<int> arr;

    for(int i = 0 ; i < n; i++){
        arr.push_back(0);
        scanf("%d", &arr.back());
    }
    
    //Binary Search
    int lo = 0, hi = n;

    while(lo < hi){
        int mid = (lo+hi)/2;

        if (check(arr, mid, tmax) == 0){
            lo = mid + 1;
        }

        else{
            hi = mid;
        }
    }

    printf("%d\n", lo);


    return 0;


}