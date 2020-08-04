#include <stdio.h>

int main(void)
{
    int year = 2020;
    if((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)//둘중 하나라도 만족하면 윤년이라고 판단 
    {
        printf("%d년은 윤년 입니다.\n", year);
    }
    else
    {
        printf("%d년은 윤년이 아닙니다.\n", year);
    }
    return 0;
}
