class Unit:
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage
    print("{0}님이 선언, 체력 : {1}, [데미지 : {2}]".format(self.name, self.hp, self.damage))

class AttackUnit(Unit):
  def __init__(self, name, hp, damage):
    Unit.__init__(self, name, hp, damage)
    self.name = name
    self.hp = hp
    self.damage = damage
  def attack(self, location):
    self.location = location
    print("{0}님이 {1}방향으로 공격".format(self.name, location))

human = AttackUnit("현준", 20, 5)
human.attack("1시")