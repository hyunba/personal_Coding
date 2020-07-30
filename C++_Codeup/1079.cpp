#include <stdio.h>
int main(void)
{
    int a;
    
    scan:
    scanf("%c", &a);
    printf("%c",a);
    if(a != 'q') goto scan;
    
    return 0;
}
