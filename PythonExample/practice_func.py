def open_account():
    print("새로운 계좌가 생성되었습니다.")

# 출력을 위해서는 이렇게 함수 이름을 적어야한다.
open_account()

def deposit(balance, money): # 입금 함수에는 잔액과 입금하는 함수가 들어감
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money # 반환된 금액을 balance로 간다.

def withdraw(balance, money):
    if balance >= money :
        print("출금이 완료되었습니다. 잔액 : {0}".format(balance - money))
        return balance - money
    else:
        print("돈이 부족합니다. 잔액 : {0}".format(balance))
        return balance

def withdraw_night(balance, money): # 저녁에 출금 시 수수료 첨부
    commission = 100
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
print(balance)
#balance = withdraw(balance, 500)
#print(balance)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원 입니다.".format(commission, balance))
