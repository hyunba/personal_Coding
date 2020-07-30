#include <stdio.h>

int main(void)
{
    long long int a,b;
    
    scanf("%lld",&a);
    reget:
    scanf("%lld", &b);
    printf("%d\n", b);
    
    if(--a!=0) goto reget;
    
    return 0;
}
