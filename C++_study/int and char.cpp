#include <stdio.h>

int main(void)
{
    char x = 'A'; // char는 하나의 문자를 담는 공간. 
    // C언어에서 char형은 내부적으로 숫자로 구성. A는 아스키코드.
    // 고로 'A' 대신 65를 입력하게되면 같은 A가 출력된다. 
    printf("%c\n", x); // %c는 하나의 캐릭터형을 출력해주는 것으로 약속. 
    
    char y = 'B';
    printf("%d", y); // 그럼 %c가 아닌 %d를 하게되면 아스키 코드 값 B가 나옴. 
    
    return 0;    
}
