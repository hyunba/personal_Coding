#include <stdio.h>

void print(int count) // count를 매개변수로 받음 
{
    if(count == 0)
    {
        return;     
    }
    else
    {
        printf("문자열을 출력합니다.\n");
        print(count - 1); // 재귀 함수 반복할 때 자기 자신을 포함하는 것. 
    }
    
}

int main(void)
{
    int number;
    printf("문자열을 몇 개 출력할까요?");
    scanf("%d", &number);
    print(number);
    
    return 0;
}
// 재귀함수는 본인 함수안에 본인이 들어가 있는 것  
