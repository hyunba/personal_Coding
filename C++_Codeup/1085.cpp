#include <stdio.h>
int main(void)
{
    double h, m, b, s;
    
    scanf("%lf%lf%lf%lf",&h,&m,&b,&s);
    printf("%.1lf MB", h*m*b*s/8/1024/1024);
    
    return 0;
}
