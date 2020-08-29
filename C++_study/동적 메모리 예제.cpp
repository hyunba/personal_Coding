#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *pi; // 포인터
    pi = (int *)malloc(sizeof(int)); // malloc = 메모리를 할당 
    if(pi == NULL)
    {
        printf("동적 메모리 할당에 실패했습니다.\n");
        exit(1);
    }
    *pi = 100;
    printf("%d\n", *pi); 
    // 동적 메모리 사용한 이후에는 모조건 해당 메모리를 반환.
    free(pi); 
    
    return 0;
}
