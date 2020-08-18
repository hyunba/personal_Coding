#include <stdio.h>
#include <string.h>

int main(void)
{
    char input[10] = "Love You";
    char result[5] = "Love";
    strcpy(result, input);
    // result 라는 문자열 안에 input 이라는 문자열을 복사 할 수 있다.
    // result는 5개의 공간 밖에 없음에도 불구하고 10개의 공간이 들어갈 수 있다.
    // strcpy는 내부적으로 포인터를 다룬다.
     
    printf("문자열 복사 : %s\n", result);
    
    return 0;
}
