#include <stdio.h>
int main(void)
{
    int a, b;
    
    scanf("%d",&a);
    for(b=1; b<=a; b++)
    {
    if(b%3==0)
    {
        printf("X ");
    }else
    {
        printf("%d ",b);
    }
    }
    return 0;
}
