class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 연습
dropship = FlyableUnit()
# 두 개 이상의 부모 클래스를 다중 상속 받게 되면 super를 사용하면
# 순서 상에 맨 마지막에 상속 받는 클래스는 사용되지 않는다.
# 그래서 다중 상속 시에는 super를 사용하지 않고 하나씩 입력해준다.