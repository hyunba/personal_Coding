#include <stdio.h>

int main(void)
{
    int score = 85;
    if(score >=90)
    {
        printf("A학점 입니다.\n");
    }
    else if(score >=80)
    {
        printf("B학점 입니다.\n");        
    }
    else if(score >=70)
    {
        printf("C학점 입니다.\n");        
    }
    else
    {
        printf("F학점 입니다.\n");
    }
    
    return 0;
}
