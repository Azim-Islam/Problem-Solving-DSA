#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <bits/stdc++.h>

using namespace std;

typedef int64_t ll;

int check(vector<vector<ll>> &arr, ll c, ll d){
    ll last = arr[0][0];
    c -= 1;
    for(ll i = 0;i < arr.size(); i++){
        ll start = arr[i][0], end = arr[i][1];
        if (last + d < start){
            last = start;
            c -= 1;
        }
        while (last + d <= end){
            last += d;
            c -= 1;
        }
    }

    if (c <=0){
        return 1;
    }
    return 0;

}

int main(){
    ll n, m;

    freopen("socdist.in", "r", stdin);
    freopen("socdist.out", "w", stdout);

    scanf("%lld %lld", &n, &m);

    vector<vector<ll>> arr;

    for(ll i = 0; i < m; i++){
        arr.push_back({0, 0});
        scanf("%lld %lld", &arr.back()[0], &arr.back()[1]);
    }

    sort(arr.begin(), arr.end());

    //Binary Search

    ll lo = 1, hi = 1e18;

    while(lo < hi){
        ll mid = lo + (hi - lo + 1) / 2;

        if(check(arr, n, mid)){
            lo = mid;
        }
        else{
            hi = mid - 1;
        }
    }
    printf("%lld\n", lo);

    

    return 0;
}