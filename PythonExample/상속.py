# 일반 유닛
class Unit: 
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit): # 괄호를 열고 상속 받고 싶은 클래스를 적어줌
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
# 상속        self.name = name # Unit이라는 클래스에 있는 정보와 같음
# 상속        self.hp = hp     # Unit이라는 클래스에 있는 정보와 같음
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]" \
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = Unit("파이어뱃", 50)
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(50)