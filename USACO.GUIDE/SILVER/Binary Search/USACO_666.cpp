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
        scanf("%lld", &arr[arr.begin() - arr.end() - 1]);
    }

    sort(arr.begin(), arr.end());

    int start, end;
    for(int i = 0; i < q; i++){
        scanf("%d %d", &start, &end);
        printf("%d", upper_bound(arr.begin(), arr.end(), end) - upper_bound(arr.begin(), arr.end(), start) - 1);
    }


    return 0;
}