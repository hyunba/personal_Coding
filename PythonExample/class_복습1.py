class Unit:
  def __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp
    self.damage = damage
    

human = Unit("현준", 20, 5)
print("{0}님이 선언되었고 체력은{1}입니다.".format(human.name, human.hp))

human2 = Unit("집에 있는 현준", 20, 1)
human2.homing = True
if human2.homing == True:
  print("{0}님은 집에 있는 상태 입니다.".format(human2.name))