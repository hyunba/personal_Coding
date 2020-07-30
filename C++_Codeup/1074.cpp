#include <stdio.h>

int main(void)
{
    long long int a;
    
    scanf("%lld", &a);
    
    while(a!=0)
    {
        printf("%d\n",a);
        a--;
    }
    return 0;
}
