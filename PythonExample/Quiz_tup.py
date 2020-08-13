from random import *
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(lst)
shuffle(lst) # list 안의 값은 무작위로 바뀜

print("-- 당첨자 발표 --")
print("치킨 당첨자 :",sample(lst, 1))
print("커피 당첨자 :",sample(lst, 3)) # 이 부분은 틀린게 치킨 당첨자가 중복될 수 있다.
print("-- 축하합니다 --")

''' 코드 수정 '''

users = range(1, 21) # 1부터 20까지 숫자를 생성
print(type(users))

users = list(users)
print(type(users))

print(users)

shuffle(users)
print(users)

winners = sample(users, 4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")