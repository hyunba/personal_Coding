''' 손님을 5번만 부른 뒤 폐기 처분 '''
# customer = "유재석"
# index = 5
# while index >= 1:
#     print("{0}, 커비가 준비 되었습니다. {1}번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

''' 손님을 계속 부름 무한루프에 빠짐 '''
# customer = "박명수"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(customer, index))
#     index +=1

customer = "노홍철"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
    if person == "노홍철" :
        print("감사합니다.")