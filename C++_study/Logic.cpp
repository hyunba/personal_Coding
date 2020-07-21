#include <stdio.h>

int main (void)
{
    int x = 50, y = 30;
    printf("x가 y보다 크고 y는 40미만인가? %d\n", (x > y) && (y < 40)); // 하나라도 틀리면 거짓 
    printf("x가 y보다 작거나 혹은 y가 30 인가? %d\n", (x < y) || (y == 30)); // 하나라도 맞으면 참 
    printf("x가 50이 아닌가? %d\n", x != 50 );
    
    return 0;   
}


 
