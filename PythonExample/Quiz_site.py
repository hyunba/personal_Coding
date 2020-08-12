site = "http://naver.com"
my_cut = site.replace("http://", "") # replace 원하는 구문을 찾음
print(my_cut)
my_cut = my_cut[:my_cut.index(".")] # my_cut[0:5] -> 0~5 직전까지
print(my_cut)
password = my_cut[:3] + str(len(my_cut)) + str(my_cut.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(site, password))