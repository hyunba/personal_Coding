def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="파이썬", age=25, name="김태호")
#순서가 뒤섞여있어도 함수가 잘 나온다.