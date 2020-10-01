class Home:
    def __init__(self, region, floor, name):
        self.region = region
        self.floor = floor
        self.name = name

class Apart(Home):
    def __init__(self, region, floor, name, apart):
        Home.__init__(self, region, floor, name)
        self.apart = apart

resident = Home("대전", "12층", "이현준")
print("{0}님은 {1}에 살며 {2}에 거주중입니다.".format(resident.name, resident.region, resident.floor))

resident2 = Apart("서울", "15층", "유재석", "반포자이")
print("{2}님은 {0}에 살며 {3}아파트 {1}에 거주중입니다.".format(resident2.region, resident2.floor, resident2.name, resident2.apart))