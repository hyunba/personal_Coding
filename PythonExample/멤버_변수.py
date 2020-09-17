class Unit: 
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

wraith1 = Unit("레이스", 80, 5)
# .을 사용해서 클래스 외부에서도 작성할 수 있다.
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.cloking = True
# 기존에는 클로킹이라는 변수는 없었지만 외부에서 추가로 할당을 해서 사용할 수 있다.
if wraith2.cloking == True: # 하지만 여기선 wraith2만 클로킹 설정을 해서 wraith1을 넣으면 오류가 나오게 된다.
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))