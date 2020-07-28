#include <stdio.h>
int main(void)
{
    long long int a;
    
    scanf("%lld",&a);
    
    if(a%2==0)
    {
        if(a>=0)
        {
            printf("%s\n","plus");
        }
        else
        {
            printf("%s\n","minus");
        }
    printf("%s\n","even");
    }
    else
    {
        if(a>=0)
        {
            printf("%s\n","plus");
        }
        else
        {
            printf("%s\n","minus");
        }
        printf("%s\n","odd");
    }
    
    return 0;
}
