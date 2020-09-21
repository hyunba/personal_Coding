try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#    nums.append(int(nums[0] / nums[1]))
#    실수로 이 부분을 입력 안했을 경우
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
# 잘 못된 값을 넣을 때 발생
except ZeroDivisionError as err:
    print(err)
# 0을 넣을 때 발생
except:
    print("알 수 없는 에러가 발생했습니다.")
# 위에 에러가 다 아닐 때 발생