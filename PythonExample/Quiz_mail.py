names = ["이현준", "신동호", "박학민", "이동일"]
for name in names:
    with open("{}.txt".format(name), "w", encoding="utf8") as email_file:
        email_file.write(f"""
안녕하세요? {name}님.

이메일은 자동적으로 보내는 메일입니다.
일단 공부중인 코드이니 그냥 보세요.
{name}님도 공부좀 하세요.""")
