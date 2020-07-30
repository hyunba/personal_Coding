#include <stdio.h>
int main(void)
{
    int a, b, sum = 0;
    
    scanf("%d",&a);
    
    for(b=0;b<=a;b++)
    {
        if(b%2==0) sum = sum + b;
    }
    printf("%d",sum);
    
    return 0;
}
