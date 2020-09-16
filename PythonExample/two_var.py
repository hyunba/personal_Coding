gun = 10 # 전역변수

def checkpoint(soldiers):
#   gun = 20 지역변수
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun 
# 원래는 이 곳에 지역변수가 없어서 결과를 얻을 수 없지만 return 을 넣어서 
# 밑에 있는 gun에서 받은 값을 리턴 받아서 계산하게 된다.


print("전체 총 : {0}".format(gun))
#checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))