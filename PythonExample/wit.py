# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 잘하고 싶어요")
# with는 pickle과 다르게 close를 안해도 된다.

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())