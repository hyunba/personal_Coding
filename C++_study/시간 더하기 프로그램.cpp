#include <stdio.h>

//전역 변수
int hour;
int minute;
int minuteAdd;

void counter() // 함수에 반환값이 없을 때 void를 사용 
{
    minute +=minuteAdd;
    hour += minute / 60;
    minute %= 60;
    hour %= 24;
}


int main(void)
{
    printf("시를 입력하세요. : ");
    scanf("%d", &hour);
    printf("분을 입력하세요. : ");
    scanf("%d", &minute); 
    printf("더할 분을 입력하세요. : ");
    scanf("%d", &minuteAdd);
    counter(); //카운터에 집어넣음 
    
    printf("더한 시간의 값은 %d시 %d분 입니다.", hour, minute);
    
    return 0;
}
