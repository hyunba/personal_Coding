// 정적 할당 : int a;
// 동적 할당 : 프로그램 실행 중에 변수를 메모리에 할당하는 것 

/*
int b; // 전역 변수는 프로그램 시작과 동시에 생기고 종료 될 때 사라진다. 

int main()
{
    int a; // a라는 지역변수는 main함수가 시작할 때 a라는 변수가 생기고 main이 끝날 때 사라진다. 
}
*/
#include <iostream>

using namespace std;

int main()
{
    int *a = new int(5); // 주솟값을 포인터에게 넘김 
    
    cout << a << endl;
    cout << *a << endl;
    
    *a = 10;
    
    cout << a << endl;
    cout << *a << endl;
    
    delete a; // 메모리 해제 
}
