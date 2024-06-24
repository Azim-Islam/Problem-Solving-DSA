#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <bits/stdc++.h>

using namespace std;

int main(){

    int t, s, p, r;
    scanf("%d", &t);

    for(int k = 1; k <= t; k++){
        
        scanf("%d %d %d", &p, &s, &r);

        if (s == p){
            if (r == 1){
                printf("Case %d: Yes\n", k);
            }
            else{
                printf("Case %d: No\n", k);
            }
        }
        else{
            printf("Case %d: Yes\n", k);
        }

    }
}