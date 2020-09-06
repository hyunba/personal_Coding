#include <stdio.h>

int main() 
{
    int a = 10;
    int b = 20;
    
    int *ptr;
    
    ptr = &a;
    printf("ptr이 가리키는 변수에 저장된 값 : %d\n", *ptr);
    
    ptr = &b;
    printf("ptr이 가리키는 변수에 저장된 값 : %d\n", *ptr);
    
    printf("b의 값 : %d\n", b);
    
    *ptr = 30; // 이 의미는 변수 b자체의 값을 30으로 주는 의미로 b값이 30으로 바뀌게 된다.  
    printf("b의 값 : %d\n", b);
    
    return 0;
}
