#include <stdio.h>
int main(void)
{
    int r, g, b, i, o, p, c=0;
    
    scanf("%d%d%d",&r,&g,&b);
    
    for(i=0; i<r; i++)
    for(o=0; o<g; o++)
    for(p=0; p<b; p++)
    {
        printf("%d %d %d\n",i,o,p);
        c++;
    }
    printf("%d",c);
    return 0;
}
