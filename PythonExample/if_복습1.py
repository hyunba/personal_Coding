absent = [1, 7]
no_book = [6]

for student in range(1,11):
  if student in absent:
    continue
  elif student in no_book:
    print("{0}번이 책이 없음"\
    .format(no_book))
    
  print("{0}번".format(student))