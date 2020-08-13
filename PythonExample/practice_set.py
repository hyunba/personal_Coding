# 집합 (set)
# 중복 x, 순서 x

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "박명수"}
python = set(["유재석", "조세호"])

# 교집합 (java와 python 둘 다 가능한 자)
print(java & python)
print(java.intersection(python))

# 합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 개발자가 생김
python.add("박명수")
print(python)

# java를 잊었다.
java.remove("김태호")
print(java)