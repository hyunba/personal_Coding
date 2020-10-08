li = [1, 5, 2, 3, 4, 8, 6, 9, 7, 15, 13, 19, 17]
n = int(input('1, 5, 2, 3, 4, 8, 6, 9, 7, 15, 13, 19, 17 : '))

s_index = 0
e_index = len(li)-1

while s_index <= e_index:
    m_index = (s_index + e_index)//2
    if n < li[m_index]:
        e_index = m_index - 1
    elif n > li[m_index]:
        s_index = m_index + 1
    else:
        print(m_index)
        break

# 선형 탐색과 다르게 이진 탐색은 점점 반씩 범위를 좁혀가면서 위치를 찾을 수 있어서 
# 더 많은 범위의 배열에서 숫자를 찾는데 효율이 좋다.
