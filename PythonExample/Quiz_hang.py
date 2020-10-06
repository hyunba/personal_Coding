from random import *
words = ["apple", "banana", "orange"]
word = choice(words)
print("answer : " + word)
letters = "" # 사용자로부터 입력받은 알파벳

while True:
    succeed = True
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print()

    if succeed:
        print("Success")
        break
    
    letter = input("Input letter > ") # 사용자 입력
    if letter not in letters:
        letters += letter
    
    if letter in word:
        print("Correct")
    else:
        print("Wrong")