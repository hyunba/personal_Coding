#include <stdio.h>
#define SECOND_PER_MINUTE 60

int main(void)
{
    int input = 1000;
    int minute = input / SECOND_PER_MINUTE;//상수로  SECOND_PER_MINUTE 60로 정의를 미리 해주었다. 
    int second = input % SECOND_PER_MINUTE; // 나눈 나머지를 초라고 정의함 
    
    printf("%d초는 %d분 %d초",input, minute, second);
        
    return 0;    
}
