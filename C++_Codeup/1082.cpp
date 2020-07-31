#include <stdio.h>
int main(void)
{
    int a, b;
    
    scanf("%X",&a);
    for(b=1; b<16; b++)
    {
        printf("%X*%X=%X\n",a,b,a*b);
    }
    
    return 0;
}
