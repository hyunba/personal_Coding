#include <stdio.h>
int main(void)
{
  long long int a;
  
  reload:
  
  scanf("%lld", &a);
  if(a==0) goto stop;
  printf("%d\n", a);
  if(a!=0) goto reload; 
  
  stop:
  
  
  return 0;
}
