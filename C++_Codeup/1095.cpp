#include <stdio.h>
int main(void)
{
    int b,i;
    int a[10000]={};
    
    scanf("%d",&b);
    
    for(i=0; i<b; i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0; i<b; i++)
    {
        a[0] = a[i-1] < a[i] ? a[i-1] : a[i]; 
    }
    printf("%d", a[0]);
    
    return 0;
}
