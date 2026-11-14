# 1. 클래스 정의 (문제의 틀)
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

# 2. 퀴즈 문제 리스트 (미리 만들어둔 문제들)
questions_list = [
    Question("대한민국의 수도는?", "서울"),
    Question("파이썬을 만든 사람은 귀도 반 ( )?", "로섬"),
    Question("사과를 영어로 하면?", "apple")
]

# 3. 퀴즈를 풀게 해주는 함수 (기능)
def run_quiz(questions):
    score = 0
    print(f"\n총 {len(questions)}문제를 시작합니다!")
    
    for q in questions:
        answer = input(f"\n{q.text} 정답 입력: ")
        # .strip()은 혹시 모를 앞뒤 공백을 지워줘요!
        if answer.strip() == q.answer:
            print("정답입니다! ✨")
            score += 1
        else:
            print(f"아쉽네요. 정답은 '{q.answer}'입니다. 😢")
            
    print(f"\n--- 퀴즈 종료! ---")
    print(f"당신의 점수: {score} / {len(questions)}")

# 4. 메뉴 화면 함수
def main_menu():
    while True:
        print("\n--- 🎮 퀴즈 게임 메뉴 ---")
        print("1. 퀴즈 풀기")
        print("2. 문제 추가하기")
        print("3. 종료")
        
        choice = input("원하는 메뉴 번호를 입력하세요: ")

        if choice == '1':
            # 여기서 위에서 만든 run_quiz 함수를 실행해요!
            run_quiz(questions_list)
               elif choice == '2':
            add_question()  # 문제 추가 함수 실행!
        elif choice == '3':
            print("\n게임을 종료합니다. 다음에 또 만나요! 👋")
            break
        else:
            print("\n[경고] 1, 2, 3 중에서만 골라주세요!")
def add_question():
    print("\n--- ➕ 새로운 문제 추가 ---")
    text = input("문제 내용을 입력하세요: ")
    answer = input("정답을 입력하세요: ")
    
    # 새로운 Question 객체를 만들어서 리스트에 추가(append)해요!
    new_q = Question(text, answer)
    questions_list.append(new_q)
    
    print("\n[성공] 문제가 리스트에 추가되었습니다! ✅")

# 5. 프로그램 시작점
if __name__ == "__main__":
    main_menu()

print("test")