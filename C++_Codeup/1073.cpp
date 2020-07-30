#include <stdio.h>
int main(void)
{
    long long int a;

    while(a!=0)
    {
        scanf("%lld", &a);
        if(a==0) goto end;
        printf("%d\n", a);
    }
    end:
    return 0;
}
