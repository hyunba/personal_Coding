# 예외 처리는 어떤 에러가 발생 했을 때 그에 대해서 처리 해주는 것
# 예를 들면 택배 기사님이 주소 배달지가 11층으로 주소가 찍혀있었지만 그 아파트는 10층만 있을 때

try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

# 잘 진행하다가 원하는 입력과 다른 에러 값이 나오면 except를 찾게된다.
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)