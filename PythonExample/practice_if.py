# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "코로나":
#     print("마스크를 챙기세요")
# else:
#     print("그냥 나가도 됩니다.")

temp = int(input("기온은 어때요? ")) # 숫자의 값으로 입력 받기 때문에 int로 감싸줌
if 30 <= temp:
    print("더워요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10 :
    print("날씨가 추워요")
else:
    print("영하의 날씨에요")