#include <stdio.h>
unsigned long long binPow(unsigned long long int a, unsigned long long int b)
{
    unsigned long long res = 1;
    while(b>0)
    {
        if(b&1) {res = res*a;}
        a = a*a;
        b >>=1;
    }
    return res;
}
int main()
{
    unsigned long long int i, t, a,b;
    scanf("%llu", &t);
    for(i=0;i<t; i++)
    {
        scanf("%llu %llu", &a, &b);
        printf("%llu\n", binPow(a,b)%10);
    }
}