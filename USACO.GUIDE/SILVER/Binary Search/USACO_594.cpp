#include <bits/stdc++.h>

using namespace std;

typedef int64_t ll;

int check(vector<ll> arr, ll R, ll K){

    for(ll i = 0; i < K; i++){
        ll start, end, m = 0;
        for(ll j = 0; j < arr.size(); j++){
            ll left, right = 0;
            for(ll t0 = j; t0 < arr.size(); t0++ ){
                if (arr[t0] <= arr[j]+R && arr[t0] >= arr[j]-R){
                    right = t0;
                }
            }
            for(ll t1 = j; t1 >= 0; t1--){
                if (arr[t1] <= arr[j]+R && arr[t1] >= arr[j]-R){
                    left = t1;
                }

            }
            if (right-left+1 > m){
                start = left;
                end = right;
            } 
        }
    }
    
}

int main(){
    

    ll n, k;
    vector<ll> arr;

    scanf("%lld %lld", &n, &k);

    for(ll i = 0; i < n; i++){
        arr.push_back(0);
        scanf("%lld", &arr.back());
    }

    sort(arr.begin(), arr.end());

    //binary search

    
    return 0;
}