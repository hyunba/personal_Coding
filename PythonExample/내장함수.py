# input : 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요?")
print("{0} 언어는 정말 좋은 언어입니다.".format(language))

# dir : 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 알려주는 것
print(dir())
import random # 외장 함수
print(dir()) # 랜덤이 추가된 모습
import pickle
print(dir()) # 피클이 추가된 모습
print(dir(random)) # 랜덤에서 사용할 수 있는 함수를 알려줌.