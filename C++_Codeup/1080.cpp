#include <stdio.h>
int main(void)
{
    int a, i,sum=0;
    
    scanf("%d",&a);
    
    for(i=1; sum<a; ++i)
    {
        sum = i + sum;
        
    }
    printf("%d",i-1);
    
    return 0;
}

