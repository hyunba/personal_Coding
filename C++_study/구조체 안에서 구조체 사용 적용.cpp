#include <stdio.h>



struct Person{
    char name[20];
    int age;
    struct Phone{
        int areacode;
        unsigned long long number;
    } phone;
};

int main()
{
    struct Person p1;
    p1.phone.areacode = 33;
    p1.phone.number = 12412412;
    
    printf("%d %llu\n", p1.phone.areacode, p1.phone.number);
    
    return 0;
}
