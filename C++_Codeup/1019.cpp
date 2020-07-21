#include <stdio.h>
int main(void)
{
    int y, m, a;
    
    scanf("%04d.%02d.%02d", &y, &m, &a);
    printf("%04d.%02d.%02d", y, m, a);
    
    return 0;
}
