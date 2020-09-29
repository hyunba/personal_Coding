person = "이현준"
costomer = "미 정"
index = 5
while person != costomer and index >= 1:
  print("{0}님 음료 준비되었습니다.\
  {1}번 남았습니다.".format(person, index))
  index -= 1
  costomer = input("성함을 말해주시겠어요?")

  if person == costomer:
    print("감사합니다.")
  elif index == 0:
    print("음료가 폐기되었습니다.")
  else:
    print("저리가세요")