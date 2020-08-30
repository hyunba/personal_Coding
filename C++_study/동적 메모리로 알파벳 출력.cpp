#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *pc = NULL; // 알파벳을 출력하기 위해 문자열 변수인 char을 써준다. 
    int i = 0;
    pc = (char *)malloc(100 * sizeof(char)); 
    // 처음 예제와 다르게 100을 곱해서 하나의 문자가 들어갈 수 있는 공간에서 100개의 문자가 들어 갈 수 있게 되었다.
    if(pc == NULL)
    {
        printf("동적 메모리 할당에 실패했습니다.\n");
        exit(1);
    }
    // pc가 가르키는 포인터를 1씩 증가 시키며 알파벳 소문자를 삽입.
    for(i = 0; i < 26; i++) // 알파벳의 갯수인 26개  
    {
        *(pc + i) = 'a' + i; // pc의 주소에 점증적으로 증가하는 i값을 더해주면서 다음 주소에 아스키코드 97인 a값을 같이 더해주면서 알파벳 순서대로 배치되게 한다. 
    }
    // 아스키 코드에서 0은 NULL을 의미한다.  
    *(pc + i) = 0;
    // 그러면 z까지 진행하다가 마지막에 NULL값이 들어가면서 문자열이 종료되게된다. 
    
    printf("%s\n", pc);
    
    free(pc);
    
    return 0;
}
