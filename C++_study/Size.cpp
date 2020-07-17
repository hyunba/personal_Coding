#include <stdio.h>

int main(void)
{
    int x; // int는 정수만 넣어줄 수 있다. x는 변수명 
    x = 5;
    printf("%d", x); // %d는 int형의 정수 값이 들어간다. 그 값은 x를 넣겠다고 선언한 것
    
    printf("변수 x의 메모리 크기는 %d 입니다.", sizeof(x)); // sizeof안에 있는 변수의 메모리 크기가 얼마나 되는지 알려줌. 
                                                            // int의 크기는 4byte로 고정됨.
     
    return 0;
}
