#include <stdio.h>
int main(void)
{
    int a, b, n, m;
    scanf("%d%d",&n,&m);
    for(a=1; a<=n; a++)
    {
        for(b=1; b<=m; b++)
        {
            printf("%d %d\n", a, b);
        }
        
    }
}

