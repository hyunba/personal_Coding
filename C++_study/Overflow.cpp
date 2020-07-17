#include <stdio.h>
#include <limits.h>


int main(void)
{
    int x = INT_MAX; // INT_MAX를 사용하려면 limits.h를 사용해야한다. 
    printf("int형의 최댓값 x는 %d입니다.\n", x);
    printf("x + 1은 %d 입니다.\n", x + 1); // 이와같이 최대값에 +1을 해주게되면 해당 값의 최소값이 나타나게 되는게 이 개념을 오버플로우라고 한다. 
    
    
    return 0;
}
