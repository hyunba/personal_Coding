class Unit: # 마린과 탱크는 유닛 클래스의 인스턴스라고 표현한다.
    def __init__(self, name, hp, damage): # self를 제외하고 주어진 갯수만큼 값을 주어야한다.
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 마린이나 탱크와 같이 클래서에서 만들어지는 것을 객체라고 한다.
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# __init__ 은 파이썬에서 쓰이는 생성자이다. 객체가 만들어질때 자동으로 호출되는 것
