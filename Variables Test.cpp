#include <stdio.h>

int main(void)
{
    int x = 50;
    float y = 123456789.2151;
    double z = 123456789.2151;
    
    printf("x = %d\n", x);
    printf("y = %.2f\n", y); // .2f는 실수를 출력하는 의미로  실수를 출력할 때 소수점 두번째 자리까지만 출력하겠다는 의미
    /*float 경우 4byte까지 자리를 차지해서 4byte에 해당하는 정보 밖에 출력을 못함.
     아무리 길게 말해도 4byte 이상이 되면 잘려나가게된다. 
     이 것을 해결하기 위해서는 우리는 double을 사용해준다.*/ 
    
    printf("z = %.2f\n", z);
    
    //double의 경우는 짤리지 않고 잘 나오게되는데 그 이유는 float과 달리 8byte의 저장공간이 존재하기 때문이다.
     
    
    return 0;
}

