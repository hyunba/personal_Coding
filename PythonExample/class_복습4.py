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
  
  def look(self, eyes):
    print("{0}님의 시력은 {1}입니다.".format(self.name, eyes))

class Childs_language:
  def __init__(self, lang):
    self.lang = lang

class Childrens(Childs, Childs_language):
  def __init__(self, name, age, hobby, lang):
    Childs.__init__(self, name, age, hobby)
    Childs_language.__init__(self, lang)
  
  def intro(self, name, age, hobby, lang):
    print("{0}님은 {1}살이며, 취미는 {2}이에요. 사용하는 언어는 {3}입니다.".format(name, age, hobby, lang))

person = Childrens("현준", 26, "코딩", "파이썬")

person.intro(person.name, person.age, person.hobby, person.lang)