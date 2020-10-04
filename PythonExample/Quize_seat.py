# for i in range(1, 21):
#     if i % 2 == 1: # i 를 2 로 나눈 나머지

#     print("A" + str(i), end = " ")

for i in range(1, 21)[::2]: # 2 칸 씩 건너 뛴다, 첫 번째랑 두 번째를 비우면 처음 부터 끝 까지라는 의미
    print("A" + str(i), end = " ")