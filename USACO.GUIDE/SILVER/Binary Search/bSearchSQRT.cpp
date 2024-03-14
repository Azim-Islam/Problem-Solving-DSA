#include <bits/stdc++.h>
using namespace std;

long long f(int x) {
    return (long long)x * x;
}

int square_root(int x) {
    int left = 0, right = x;
    while (left < right) {
        int middle = (left + right) / 2;
        if (f(middle) <= x) {
            left = middle;
        } else {
            right = middle - 1;
        }
    }
    return left;
}


int main()
{
    double d = square_root(4);

    cout << d;
    return 0;
}
