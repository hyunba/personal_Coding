# print("Python", "Java", "javaScript", sep=" vs ") # sep를 선언하면 자기가 원하는 대로 콤마를 변형할 수 있다.
# print("Python", "Java", "javaScript", sep=",", end="?") # end를 적으면 한줄로 나오게 된다. 문장의 끝부분을 물음표로 바꿔주세요 라는 뜻

# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력으로 처리
# print("Python", "Java", file=sys.stderr) # 표준 에러로 처리

# 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): 

#     print(subject.ljust(8), str(score).rjust(4), sep= ":") # ljust 좌측 정렬하고 8칸 띄움 rjust 우측 정렬한후 4칸 띄움

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21): # num 변수를 만들고 1 부터 21 이전까지 숫자를 range로 만들어서 출력
#     print("대기번호 : " + str(num).zfill(3)) # zfill 0을 채움

answer = input("아무 값이나 입력하세요 : ") # 실행을하면 커서가 껌뻑이면서 사용자 입력을 대기함
print("입력하신 값은 " + answer + "입니다.") # 숫자를 할 때는 str으로 감싸줘야 하는데 이상없이 됨
# 그 이유는 사용자 입력을 받으면 항상 문자열로 인식을 한다는

