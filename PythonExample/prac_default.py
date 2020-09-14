#def profile(name, age, main_lang):
#    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
#        .format(name, age, main_lang))

#profile("유재석", 20, "파이썬")
#profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.

def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
        .format(name, age, main_lang))

profile("유재석")
profile("김태호")

# 위에 주석처리 된 예와 다르게 밑에서는 이름만 주어졌지만
# 정의된 프로필에 직접 정의를 내려주면 둘다 같은 값이 나오게된다.