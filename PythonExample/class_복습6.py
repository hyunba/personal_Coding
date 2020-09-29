class Travle:
  def __init__(self, name, region, age):
    self.name = name
    self.region = region
    self.age = age

    print("{0} 회원님이 등록되었습니다.".format(name))

  def move(self, location):
    print("{0} 회원님이 {1}로 이동하고 계십니다."\
    .format(self.name, location))
  
  def home(self, ret):
    print("{0} 회원님이 다시 돌아왔습니다."\
    .format(self.name))
  
# hyunjun1 = Unit("이현준", "대전", 26)
# hyunjun1.move("서울")

print("입력해주세요")
hyunjun1 = Travle(input("이름"), input("지역"), input("나이"))
hyunjun1.move(input("어디로 가시겠습니까?"))
ret = input("집으로 가시게습니까? y/n")
p = "y"
while ret != p:
  if ret == "y":
    print("집으로 이동")
    break