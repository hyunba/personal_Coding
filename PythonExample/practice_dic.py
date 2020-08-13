# cabinet = {3:"유재석", 100:"김태호"} # 3번 키를 유재석 씨가 받아감, 100번 키는 김태호 씨가 받아감

# # 호출 방법 1
# print(cabinet[3])
# print(cabinet[100]) # 값이 없으면 오류를 출력하고 프로그램 종료

# # 호출 방법 2
# print(cabinet.get(3)) # 값이 없으면 None으로 출력하고 다음 코드를 실행

# # None 활용
# print(cabinet.get(5, "사용 가능"))

# # 값이 있는지 확인하기
# print(3 in cabinet) # True
# print(5 in cabinet) # False

cabinet = {"A-3" : "유재석", "C-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["C-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "박명수"
cabinet["C-20"] = "하하"
print(cabinet)

# 나간 손님
del cabinet["C-20"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)