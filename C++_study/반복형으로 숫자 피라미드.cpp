#include <stdio.h>

int print(int a)
{
    int i, j;
    for(i = 0; i < a; i++) // a번 이 부분을 반복. 
    {
        for(j = 0; j <= i; j++) // i까지 출력 
        {
            printf("%d ", j + 1);
        }
        printf("\n"); // 한바퀴 돌게되면 줄바꿈 
    }
    
}

int main(void)
{
    int a;
    scanf("%d", &a);
    print(a); // a값을 넣음 
    
    return 0;
}
