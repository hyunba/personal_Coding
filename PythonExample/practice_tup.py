# 튜플은 리스트와 다르게 내용을 변경하거나 추가할 수 없다.
# 하지만 속도가 리스트보다 빠르다
# 그래서 변경되지 않는 내용들을 다룰 때 튜플을 이용하면 유용하다.

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name = "이현준"
age = 26
hobby = "코딩"

print(name, age, hobby)

(name, age, hobby) = ("이현준", 26, "코딩")
print(name, age, hobby)