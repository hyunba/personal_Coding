#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *pi, i;
    pi = (int *)malloc(5 * sizeof(int));
    if(pi == NULL)
    {
        printf("동적 메모리 할당에 실패했습니다.\n");
        exit(1);
    }
    pi[0] = 100;
    pi[1] = 200;
    pi[2] = 300;
    pi[3] = 400;
    pi[4] = 500;
    
    for(i = 0; i < 5; i++)
    {
        printf("%d\n", *(pi + i)); // 배열과 포인터 변수는 밀접한 관계가 있다. 
    }
    // pi[0] = *(pi + 0) 같은 의미 
    
    free(pi);
    
    return 0;
}
