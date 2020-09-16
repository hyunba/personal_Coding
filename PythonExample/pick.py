# pickle은 프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장하는 것
import pickle
 profile_file = open("profile.pickle", "wb") # w는 쓰기 목적, b는 바이너리 파일
 profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
 print(profile)
# pickle을 이용해서 이 데이터를 파일에다 쓰는 것 prifile 에 있는 정보를 파일에 저장하는 것
 pickle.dump(profile, profile_file) 
# profile_file.close()


#profile_file = open("profile.pickle", "rb")
#profile = pickle.load(profile_file)
#print(profile)
profile_file.close()