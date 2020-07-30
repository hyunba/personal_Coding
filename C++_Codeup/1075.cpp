#include <stdio.h>

int main(void)
{
    long long int a;
    
    scanf("%lld", &a);
    
    while(a!=0)
    {
        a--;
        printf("%d\n",a);
    }
    return 0;
}

