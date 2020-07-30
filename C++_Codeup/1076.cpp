#include <stdio.h>

int main(void)
{
    int a,b='a';
    
    scanf("%c",&a);
    do
    {
        printf("%c\n",b);
        b++;
    }while(b<a+1);
    
    return 0;
}
