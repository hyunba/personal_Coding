def std_weight(height, gender): # 키는 m 단위(실수), 170cm 경우 1.7
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2) # /100을 한 이유는 m 단위로 했기 때문
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

