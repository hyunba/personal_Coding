#include <stdio.h>
#include <math.h> // pow(), abs()가 존재한다. 

int main(void)
{
    double x = pow(2.0, 20.0);  // 왼쪽에 있는 숫자가 오른쪽 만큼 거듭제곱이 일어난다는 의미. (2의 20제곱) 
    printf("2의 20제곱은 %.2f입니다.\n", x); //.2f는 소숫점 둘 째 자리까지 보여줌. .0f를 하면 정수 부분만 보여줌. 
    return 0;    
}
