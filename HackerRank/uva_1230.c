#include <stdio.h>
unsigned long long binPowMod(unsigned long long x, unsigned long long y, unsigned long long m)
{
    x=x%m;
    unsigned long long result=1;
    while(y>0)
    {
        if(y&1) {result = (x*result)%m;}
        x = (x*x)%m;
        y >>= 1;
    }
    return result;

}
int main()
{
    unsigned long long i, t, x,y,z;
    scanf("%llu", &t);
    for(i=0;i<t;i++)
    {
        scanf("%llu %llu %llu", &x, &y, &z);
        printf("%llu\n", binPowMod(x,y,z));
    }
    scanf("%llu", &t);
    return 0;
}