person = "이현준"
costomer = "미 정"
while person != costomer:
  print("{0}님 음료 준비되었습니다.\
  ".format(person))
  costomer = input("성함을 말해주시겠어요?")

  if person == costomer:
    print("감사합니다.")
  else:
    print("저리가세요")