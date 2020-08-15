absent = [2, 5]
no_book =[7]

for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}번은 교무실로 오세요".format(no_book))
        break
    print("{0}번, 책을 읽어주세요".format(student))