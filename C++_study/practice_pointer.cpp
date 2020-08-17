#include <stdio.h>

int main(void)
{
    int x = 50;
    int *y = &x;
    
    printf("%d", y);
    printf("%d", *y);
    
    return 0;
}
