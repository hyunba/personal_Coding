class Word:
    def __init__(self, word, ex1, ex2, answer):
#       pass
        self.word = word # 멤버 변수 설정.
        self.ex1 = ex1
        self.ex2 = ex2
        self.answer = answer

    def show_question(self):
#       pass
        print(f"\"{self.word}\"의 뜻은?")
        print("1." + self.ex1)
        print("2." + self.ex2)

    def check_answer(self, user_input):
#       pass
        if user_input == self.answer:
            print("정답입니다.")
        else:
            print("틀렸습니다.")


word = Word("별다줄", "별걸 다 줄이네", "별 다방 줄 길다", 1)
word.show_question()
word.check_answer(int(input("=>")))