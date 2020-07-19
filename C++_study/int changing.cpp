#include <stdio.h>

int main(void)
{
    int a = 100;
    
    printf("10진수로 출력 : %d\n", a);
    printf("8진수로 출력 : %o\n", a); // %o를 하게되면 8진수로 표현이 된다. 
    printf("16진수로 출력 : %x\n", a);// %x를 하게되면 16진수로 표현이 된다. 
    
    return 0;
}
