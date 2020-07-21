#include <stdio.h>

int main(void)
{
    int x = 50, y = 30;
    // x = y -> x와 y가 같은 상황 의미.
    // x == y -> true, x와 y가 같은 값을 갖는지 판별하는 것. 
    
    printf("x가 y와 같은가? %d\n", x==y); // 0은 거짓 
    printf("x가 y와 다른가? %d\n", x!=y); // 1은  참 
    printf("x가 y와 큰가? %d\n", x > y);
    printf("x가 y와 작은가? %d\n", x < y);
    printf("x에 y값을 넣으면? %d\n", x=y);
    
    if(x == y)
    {
     // x와 y가 참일 경우 이 부분 실행   
    }행 
    else
    {
     // 아닐 경우 이 부분 실   
    }

    
    return 0;
}
