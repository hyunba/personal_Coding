#include <stdio.h>
int main(void)
{
    FILE *fp = NULL ;
    fp = fopen("Hello.txt", "w");
    if(fp == NULL)
    {
        printf("파일 열기에 실패했습니다.\n");    
    }
    else
    {
        printf("파일 열기에 성공했습니다.\n");
    }
    fputc('H', fp);
    fputc('E', fp);
    fputc('L', fp);
    fputc('L', fp);
    fputc('O', fp);
    fclose(fp);
    // 두 번 실행 한다고 해서 두번 HELLO가 출력되는 것은 아님 
    return 0;    
}
