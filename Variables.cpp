#include <stdio.h>

int main(void)
{
    int x = 10;
    int y = 20;
    
    printf("x = %d입니다.\n", x);
    printf("y = %d입니다.\n", y);
    printf("x + y = %d입니다.\n", x + y);
    printf("x - y = %d입니다.\n", x - y);
    printf("x * y = %d입니다.\n", x * y);
    printf("x / y = %d입니다.\n", x / y); // 하지만 우리는 int형을 썼기 때문에 몫의 값 0만 나오게된다. 
       
    return 0;    
}
