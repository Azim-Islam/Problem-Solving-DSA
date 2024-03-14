#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#include <bits/stdc++.h>


using namespace std;
typedef int64_t ll;


int main(){
    
    freopen("haybales.in", "r", stdin);
    freopen("haybales.out", "w", stdout);

    int n, q;
    scanf("%d %d", &n, &q);

    vector<ll> arr;

    for(int i = 0; i < n ; i++){
        arr.push_back(0);
        scanf("%ld", &arr.back());
    }

    sort(arr.begin(), arr.end());



    int start, end;
    for(int i = 0; i < q; i++){
        scanf("%d %d", &start, &end);
        int v1 = upper_bound(arr.begin(), arr.end(), end) - arr.begin();
        int v2 = lower_bound(arr.begin(), arr.end(), start) - arr.begin();
        printf("%d\n", v1 - v2);
    }


    return 0;
}