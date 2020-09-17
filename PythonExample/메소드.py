class Unit: 
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
# self는 자기자신 클래스 앞에선 무조건 self를 사용
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]" \
            .format(self.name, location, self.damage))
# self를 사용하면 여기서는 __init__에 저장된 값이 사용되어지고 self가 없는 location에는 attack에 들어가있는 값이 적용되어진다.

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = Unit("파이어뱃", 50, 16)
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(50)