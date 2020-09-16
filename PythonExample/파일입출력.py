# score_file = open("score.txt", "w", encoding="utf8") # "w"를 입력해서 우리는 입력할꺼라고 선언하고 encoding utf8을 해야 우리는 한글을 이상없이 사용할 수 있다.
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close() # 연 파일을 닫아줌

# 총 정리를 하자면 score_file을 입력 목적으로 열어서 내용을 파일에 쓰고 파일을 닫음.

# score_file = open("score.txt", "a", encoding="utf8") # 위에 내용처럼 w를 또 사용하게 되면 score.txt에 덮어쓰기가 되므로 이어서 작성하고 싶으면 a를 입력해준다.
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read()) # 한번에 파일의 모든 내용을 다읽음
# score_file.close()


# 한줄씩 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 한줄만 읽는데 커서는 다음줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 위에서 명시한 한줄씩 읽기는 우리가 4줄 이라는 것을 알고 print로 출력을 했지만 다른사람이 파일을 생성할 경우 몇 글자인지 모르므로 while을 사용해서 출력해보자.
# score_file = open("score.txt", "r", encoding="utf8")
# while True: # true 무한루프 
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()