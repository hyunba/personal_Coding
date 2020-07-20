#include <stdio.h>

int main(void)
{
    int x = 100;
    printf("현재 x의 값은 %d입니다.\n", x);
    x += 50; // x = x + 50 
    printf("현재 x의 값은 %d입니다.\n", x);
    x -= 50; // x = x - 50, 현재 x는 150이므로 100이 출력된다. 
    printf("현재 x의 값은 %d입니다.\n", x);
    x *= 50;
    printf("현재 x의 값은 %d입니다.\n", x);
    x /= 50;
    printf("현재 x의 값은 %d입니다.\n", x);
    x %= 3; // 100을 3으로 나눈 나머지 값을 구하므로 1이 됨. 
    printf("현재 x의 값은 %d입니다.\n", x); 
    
    return 0;
}
