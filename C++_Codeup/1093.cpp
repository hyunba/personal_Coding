#include<stdio.h>
int main(void)
{
    int b,c,i;
    int a[24]={};
    
    scanf("%d",&b);
    
    for(i=1; i<=b; i++)
    {
        scanf("%d",&c);
        a[c]=a[c]+1;
    }
    for(i=1; i<=23; i++)
    {
        printf("%d ",a[i]);
    }
    return 0;
}

