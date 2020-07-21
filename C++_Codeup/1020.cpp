#include <stdio.h>
int main(void)
{
    int y, m, n, r, a, t;
    
    scanf("%02d%02d%02d-%02d%02d%03d", &y, &m, &n, &r, &a, &t);
    printf("%02d%02d%02d%02d%02d%03d", y, m, n, r, a, t);
    
    return 0;
}
