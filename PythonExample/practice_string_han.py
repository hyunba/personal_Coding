python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper()) # 첫 번째 문자가 대문자인지 참,거짓
print(len(python)) # 빈공간 포함해서 글자 수
print(python.replace("Python", "C language"))

index = python.index("n")
print(index) # n이 몇번째에 있는지 출력
index = python.index("n", index + 1) # 기존의 위치에서 다음 단계부터 두번째 n 위치가 어딨는지 검색
print(index) # n 두번째 위치 출력

print(python.find("C language")) # C 언어를 찾다가 없으면 -1 출력
#print(python.index("C language")) # 자바라는 단어가 없기 때문에 에러

print(python.count("n")) # python에서 n이 몇번째 출력되는지