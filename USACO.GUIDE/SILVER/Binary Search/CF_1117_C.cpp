#include <bits/stdc++.h>
using namespace std;
typedef int64_t ll;

bool check(ll x1, ll y1, ll x2, ll y2, ll time, string s){
    ll wind_x = 0;
    ll wind_y = 0;

    for(auto c: s){
        if (c == 'U') wind_y += 1;
        if (c == 'D') wind_y -= 1;
        if (c == 'L') wind_x -= 1;
        if (c == 'R') wind_x += 1;
    }

    wind_x = wind_x * (time/s.size());
    wind_y = wind_y * (time/s.size());

    for(ll i = 0; i < time%s.size(); i++){
        auto c = s[i];
        if (c == 'U') wind_y += 1;
        if (c == 'D') wind_y -= 1;
        if (c == 'L') wind_x -= 1;
        if (c == 'R') wind_x += 1;
    }
    x1 += wind_x;
    y1 += wind_y;

    return abs(x1 - x2) + abs(y1 - y2) <= time;
}


int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);


    ll x1, y1, x2, y2, n;

    string s;
    // scanf("%ld %ld", &x1, &y1);
    // scanf("%ld %ld", &x2, &y2);
    // scanf("%ld", &n);
    cin >> x1 >> y1;
    cin >> x2 >> y2;
    cin >> n;

    // getline(cin, s);
    cin >> s;


    ll lo = 1;
    ll hi = 1e15;
    ll valid = -1;

    while(hi > lo){
        ll mid = (hi+lo)/2;
        if (check(x1, y1, x2, y2, mid, s)){
            valid = mid;
            hi = mid;
        }
        else{
            lo = mid + 1;
        }
    }
    cout << valid << '\n';




    return 0;
}