#include <stdio.h>

struct food {
    char name[10];
};

int main(void)
{
    struct food a;
    
    printf("등록하실 과일을 입력해주세요. :");
    scanf("%s", &a.name);
    
    printf("등록된 과일은 %s 입니다.", a.name);
    
    return 0;
}
