#include <stdio.h>

int main(void)
{
    int number, x, i, sum = 0;
    
    printf("정수의 갯수를 입력하세요. : ");
    
    scanf("%d", &number);
    
    for(i = 0; i < number; i++)
    {
        printf("정수를 입력하세요. : ");
        scanf("%d",&x);
        sum += x;        
    }
    printf("정해진 갯수의 합 : %d\n", sum);
    
    return 0;
}

 
