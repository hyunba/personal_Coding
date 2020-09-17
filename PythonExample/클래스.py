name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("{0}, 공격력 {1}\n".format(hp, damage))

# 탱크 
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("{0}, 공격력 {1}\n".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("{0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

def attack(name, location, damage) :  # 어택이라는 함수 생성
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

# 유닛은 한마리 한마리 씩 해주면 한도 끝도 없기 때문에 Class가 필요하게 된다.
# Class 는 붕어빵 틀과 같다
