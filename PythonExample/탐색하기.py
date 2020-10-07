li = [1,2,3,4,5,6,10,8,7,9]
n = int(input('1~10'"사이의 값을 입력하세요 : "))

for i in range(len(li)):
    if li[i] == n:
        print(i)
        break