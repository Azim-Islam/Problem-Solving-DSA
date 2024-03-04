#include <bits/stdc++.h>



using namespace std;
typedef long long ll;


int check(vector<ll> &arr, ll m, ll c, ll x){
    //we check if for value of 'x' if arrangement is possible

    vector<vector<ll>> container;
    for(int i = 0; i < m; i++){
        container.push_back({});
    }
    
    ll ptr = 0;

    for(int i = 0; i < arr.size(); i++){
        if(ptr >= m){
            return 0;
        }
        if(container[ptr].size() < c){ 
                if(container[ptr].size() == 0){
                    container[ptr].push_back(arr[i]);

                }
                else if (arr[i] - container[ptr][0] <= x){
                    container[ptr].push_back(arr[i]);
                }
                else if (arr[i] - container[ptr][0] > x){
                    i--;
                    ptr++;
                }

            }
        else{
            i--;
            ptr++;
            }
    }
    // printf("Possible for %lld\n", x);
    return 1;

} 



int main(){
    freopen("convention.in", "r", stdin);
    freopen("convention.out", "w", stdout);

    ll n, m, c;
    scanf("%lld %lld %lld", &n, &m, &c);

    vector<ll> arr;


    for(int i =0 ; i < n; i++){
        arr.push_back(0);
        scanf("%lld", &arr.back());
    }

    sort(arr.begin(), arr.end());

    //BINARY SEARCH
    ll hi = 1e18, lo = 0, mid;

    while(lo < hi){
        mid = (hi+lo)/2;
        if(check(arr, m, c, mid) == 1){
            hi = mid;
        }
        else{
            lo = mid + 1;
        }
    }

    printf("%lld\n", hi);




}