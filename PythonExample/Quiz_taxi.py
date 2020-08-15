# from random import *
# time = randint(5, 51)
# want_time = randint(5, 16)

# for person in range(1, 51):
#     print("{0}번째, 손님 (소요시간 :{1})".format(person, time))

''' 코드 수정 '''
from random import *
cnt = 0 # 총 탑승 승객
for i in range(1, 51): # 1 ~ 50 승객 수
    time = randrange(5, 51) # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
            
print("총 탑승 승객 :",cnt,"분")
