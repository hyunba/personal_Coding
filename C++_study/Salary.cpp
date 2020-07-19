#include <stdio.h>
#define MONTHS 12
//상수에 대한 정의를 해주는 것.

int main(void)
{
    double monthSalary = 1244.3; 
    printf("$ %.2f", monthSalary * MONTHS);//.2f는 소숫점 두자리까지만 구현. 
    
    return 0;
}
