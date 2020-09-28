def open_account():
  print("계좌 생성")

open_account()

def deposit(balance, money):
  print("입금 완료. 잔액 : {0}"\
  .format(balance + money))
  return balance + money

def withdraw(balance, money):
  if balance >= money :
    print("출금 완료. 잔액 : {0}"\
    .format(balance - money))
    return balance - money
  else :
    print("돈이 부족합니다. \
    잔액 : {0}".format(balance))
    return balance

balance = 0
balance = deposit(balance, 1000)

print(balance)