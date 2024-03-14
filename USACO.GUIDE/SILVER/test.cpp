#include <bits/stdc++.h> 
using namespace std;

typedef long long int ll;

int main(){
    ll n, m, q;
    scanf("%lld %lld %lld", &n, &m, &q);

    vector<vector<ll>> d;
    vector<ll> marr;
    for(ll i = 0; i < m; i++){
        vector<ll> l;
        d.push_back(l);
    }

    for(ll i = 0 ; i < n ; i++){
        ll p, idx;
        scanf("%lld %lld", &p, &idx);
        d[idx-1].push_back(p);
    }
    
    for(ll i = 0; i < m; i++){
        scanf("%lld", &marr[i]);
    }

    for(ll i=0; i<d.size(); i++){
        sort(d[i].begin(), d[i].end(), greater<>());
    }

    ll dc = 0;

    for(ll i = 0; i < m; i++){
        for(ll k = d[i].size()-1; k > -1; k--){
            ll t = min(d[i][k], marr[i]);
            d[i][k] -= t;
            marr[i] -= t;
            if (d[i][k] == 0){
                dc += 1;
                d[i].pop_back();
            }
            if (marr[k] == 0){
                break;
            }
        }
    }

    vector<ll> arr = {0};

    for(ll i = 0; i < d.size(); i++){
        for(ll k = 0; k < d[i].size(); k++){
            arr.push_back(d[i][k]);
        }
    }

    sort(arr.begin(), arr.end());

    for(ll i = 1; i<arr.size(); i++){
        arr[i] = arr[i] + arr[i-1];
    }

    for(ll i = 0; i < q; i++){
        ll t;
        scanf("%lld", &t);
        auto it = upper_bound(arr.begin(), arr.end(), t);
        ll index = distance(arr.begin(), it);
        printf("%lld\n", index-1+dc);
    }


}