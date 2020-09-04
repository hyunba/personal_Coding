#include <stdio.h>

int main(void)
{
    int a;
    int arr[1000];
    
    printf("입력할 숫자의 갯수 입력: ");
    scanf("%d", &a);
    for(int i = 0; i < a; i++)
    {
        scanf("%d", &arr[i]);
    }
    for (int i = a-1; i >= 0; i--)
    {
        printf("%d ", arr[i]);
    }
    
    
    return 0;
}
