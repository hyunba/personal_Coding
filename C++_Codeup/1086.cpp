#include <stdio.h>
int main(void)
{
    double w, h, p;
    
    scanf("%lf%lf%lf%lf",&w,&h,&p);
    printf("%.2lf MB", w*h*p/8/1024/1024);
    
    return 0;
}
