#include <bits/stdc++.h>

using namespace std;

typedef int64_t ll;

int check(vector<ll> &arr, double R, double pos){
    auto lidx = lower_bound(arr.begin(), arr.end(), pos-R) - arr.begin();
    auto ridx = upper_bound(arr.begin(), arr.end(), pos+R) - arr.begin() - 1;
    double RR = R;
    
    ll prev_idx;

    while (R-1 >= 0 && lidx > 0){
        prev_idx = lidx;
        R -= 1;
        // lidx = lower_bound(arr.begin(), arr.begin()+lidx, arr[lidx]-R) - arr.begin();
        lidx = lower_bound(arr.begin(), arr.end(), arr[lidx]-R) - arr.begin();

        if (lidx == prev_idx){
            return 0;
        }
        else{
            prev_idx = lidx;
        }
    }

    while (RR-1 >= 0 && ridx < arr.size() - 1){
        prev_idx = ridx;
        RR -= 1;

        // ridx = upper_bound(arr.begin()+ridx, arr.end(), arr[ridx]+RR) - arr.begin() - 1;
        ridx = upper_bound(arr.begin(), arr.end(), arr[ridx]+RR) - arr.begin() - 1;
        
        if (ridx == prev_idx){
            return 0;
        }
        else{
            prev_idx = ridx;
        }
    }
    if (lidx == 0 && ridx == arr.size()-1){
        return 1;
    }
    return 0;
}



int check_Pos(vector<ll> &arr, double R){
    for(int i=0; i < arr.size(); i++){
        double pos = arr[i]+R;
        if (check(arr, R, pos) == 1){
            // printf("Correct for R = %lf POS = %ld", R, pos);
            return 1;
        }
        else{
        }
    }
    return 0;
}



int main(){
    
    freopen("angry.in", "r", stdin);
    freopen("angry.out", "w", stdout);

    ll n;
    scanf("%ld", &n);
    vector<ll> arr;
    for(ll i = 0; i < n; i ++){
        arr.push_back(0);
        scanf("%ld", &arr.back());
    }

    sort(arr.begin(), arr.end());
    double lo = 0;
    double hi = 1e9;
    while (hi - lo > 0.01){
        double mid = (lo + hi)/2.0;
        if (check_Pos(arr, mid) == 1) {
            hi = mid;
        }
        else{
            lo = mid;

        }
    }
    // printf("%d\n", check_Pos(arr, 24197.0));

    printf("%0.1lf\n", hi);
    // for(int i = arr[0]; i <= arr.back(); i++){
    //     printf("%d %d\n", i, check_R(arr, i));
    // }
    
    
}