#include<stdio.h>

int main(void)
{
    long long int a, m, d, n,c=1;
    
    scanf("%lld%lld%lld%lld",&a,&m,&d,&n);
    
    for(a;c<n;c++)
    {
            a = a*m+d;
    }
    printf("%lld",a);
    
    return 0;
}

