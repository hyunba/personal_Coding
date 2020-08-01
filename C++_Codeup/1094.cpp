#include<stdio.h>
int main(void)
{
    int a, c, i;
    int b[10000]={};
    scanf("%d",&a);
    
    for(i=1; i<=a; i++)
        scanf("%d",&b[i]);
        
    for(i=a; i>=1; i--)
        printf("%d ",b[i]);
    
    return 0;
}

