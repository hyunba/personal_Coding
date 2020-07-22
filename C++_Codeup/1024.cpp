#include <stdio.h>
int main(void)
{
    char e[30];
    int i;
    
    scanf("%s", &e);
    
    for(i=0; e[i]!='\0'; i++){
    printf("\'%c\'\n", e[i]);
    }
    
    return 0;
}

