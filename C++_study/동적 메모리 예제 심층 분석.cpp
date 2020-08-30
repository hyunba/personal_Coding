#include <stdio.h>
#include <stdlib.h> 
// 동적 메모리를 사용하기 위해서 필수적으로 사용해야함 

int main(void)
{
    int *pi; // 포인터, 기본적인 변수 생성 
    pi = (int *)malloc(sizeof(int)); // malloc = 메모리를 할당 (sizeof(int)) = 인트 형의 크기만큼 할당. 
    if(pi == NULL)
    {
        printf("동적 메모리 할당에 실패했습니다.\n");
        exit(1); // 프로그램을 종료. 
    }
    *pi = 100; // 이 pi 라는 포인터 변수가 가리키고 있는 그 주소의 값에 100을 넣는다. 
    printf("%d\n", *pi); 
    // 동적 메모리 사용한 이후에는 모조건 해당 메모리를 반환.
    // 그 이유는 전반적으로 시스템의 안정성을 높이고 메모리의 효율성을 높이기 위해 사용. 
    free(pi); // pi 포인터 변수가 가리키고 있는 메모리 주소에 메모리 할다을 해제함. 
    // 해제 하는 곳은  (int *)malloc(sizeof(int)); 4바이트 만큼의 크기의 메모리를 해제. 
    
    return 0;
}
