from random import *

print(random()) # 랜덤 함수를 통해 0.0 ~ 1.0 미만의 난수를 뽑는 것
print(random() * 10) # 0.0 ~ 10.0 미만
print(int(random() * 10)) # 0 ~ 10 미만 소숫점을 없애기 위해 int 사용
print(int(random() * 10)+ 1) # 1 ~ 10 이하의 랜덤 값 출력