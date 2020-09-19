class Parents:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Childs(Parents):
  def __init__(self, name, age, hobby):
    Parents.__init__(self, name, age)
    self.hobby = hobby
  
  def loc(self, location):
    print("{0}님이 : {1}방향으로 갑니다.".format(self.name, location))

person = Parents("현준",26)
person = Childs("현준",26,"코딩")
person.loc("동쪽")