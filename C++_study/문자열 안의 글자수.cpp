#include <stdio.h>
int main(void)
{
    // 영어 : 1개 크기 (1byte), 한글 : 2개 크기 (2byte) 
    // array[10]일 경우 영어는 10개의 문자, 한글은 5개의 문자 가능.
    char input[1001];
    gets(input);
    int count = 0;
    while(input[count] != '\0')
    {
        count++;
    }
    printf("입력한 문자열의 길이는 %d입니다.", count);
    printf("입력한 문자열은 : %s 입니다.", input);
    
    return 0;
}
