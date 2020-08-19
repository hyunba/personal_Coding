#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct student {
    int number;
    char name[10];
    double grade;
};

int main(void)
{
    struct student s; // 구조체 student 변수 s 라는 의미
    s.number = 20150001;// s 라는 구조체에 number라는 값을 넣을 수 있게됨. 
    strcpy(s.name, "이현준");
    
    s.grade = 4.5;
    printf("학번 : %d\n", s.number);
    printf("이름 : %s\n", s.name);
    printf("학점 : %.lf\n", s.grade);
    
    return 0;    
}
