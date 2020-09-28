temp = int(input("기온을 적어주세요"))

if temp >= 30 :
  print("더워요")
elif temp <= 29 and temp > 15 :
  print("선선해요")
elif temp <= 14 and temp > 0 :
  print("쌀쌀해요")
else :
  print("추워요")