#include <bits/stdc++.h>
using namespace std;
typedef int64_t ll;

int main(){
    ll t;
    scanf("%ld", &t);
    while(t--){
        vector<ll> arr;
        priority_queue<ll, vector<ll>, greater<ll>> pq;
        ll N, P, X, A, count = 0;
        scanf("%ld %ld %ld %ld", &N, &P, &X, &A);
        P += X;
        for(int i = 0; i < N; i++){
            arr.push_back(0);
            scanf("%ld", &arr.back());
        }
        for(int i = 0; i<N; i++){
            if (pq.size() < A){
                pq.push(arr[i]);
                count += 1;
            }
            else{
                pq.push(arr[i]);
                ll v = pq.top();
                pq.pop();

                if (P - v >= 0){
                    P = P - v;
                    count += 1;
                }
                else{
                    break;
                }

            }
        }
        printf("%ld\n", count);
    }
}