#include <stdio.h>

int main(void)
{
    int a = 20;
    
    int byunsoo; // 일반적인 변수 선언 
    
    int *ptr_a; // 포인터 선언 
    
    char *ptr_c; // 문자 정수 포인터 선언
    
    ptr_a = &a; // &는 주소값이므로 a의 주소값을 의미 
    
    printf("%d\n", ptr_a); // 주소값을 나타냄 주소값은 램 상황에 따라 계속해서 바뀌어감
    
    printf("a의 값: %d\n", a);
    printf("a의 주솟값: %d\n", &a);
    printf("ptr_a에 저장된 값 : %d\n", ptr_a);
    printf("ptr_a가 가리키는 변수의 값 : %d\n", *ptr_a); // 포인터는 그 해당 주소의 값의 변수의 값을 알려줌 
    
    return 0;
}
