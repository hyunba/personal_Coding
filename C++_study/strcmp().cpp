#include <stdio.h>
#include <string.h>

int main(void)
{
    char inputOne[5] = "A";
    char inputTwo[5] = "B";
    printf("문자열 비교 : %d\n", strcmp(inputOne, inputTwo));
    // 두 문자가 사전적으로 동일하면 '0'이 나오고, 왼쪽에 있는게 더 앞에있다면 '-1' 
    // 오른쪽이 더 앞이면 '1'로  나오게 된다. 
    
    return 0;
}
