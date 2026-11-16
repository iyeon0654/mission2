import json

# 1. 클래스 정의 (문제의 틀)
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question    # 문제 내용
        self.choices = choices      # 선택지 4개 (리스트!)
        self.answer = answer        # 정답 번호 (1~4)

# 2. 퀴즈 문제 리스트
# (프로그램 맨 아래 __main__ 에서 불러올 거예요!)

# 3. 퀴즈를 풀게 해주는 함수 (기능)
def run_quiz(quizzes):
    score = 0
    print(f"\n총 {len(quizzes)}문제를 시작합니다!")

    for q in quizzes:
        print(f"\n{q.question}")        # 문제 보여주기

        # 선택지 4개를 번호와 함께 보여줘요!
        for i in range(len(q.choices)):
            print(f"  {i + 1}) {q.choices[i]}")

        answer = input("정답 번호를 입력하세요 (1~4): ")

        # 입력한 번호와 정답 번호를 비교해요!
        if answer.strip() == str(q.answer):
            print("정답입니다! ✨")
            score += 1
        else:
            print(f"아쉽네요. 정답은 {q.answer}번 입니다. 😥")

    print(f"\n--- 퀴즈 종료! ---")
    print(f"당신의 점수: {score} / {len(quizzes)}")

    # 4. 문제들을 파일에 저장하는 함수
def save_questions(questions):
    # 붕어빵(객체)들을 딕셔너리 목록으로 바꿔 담을 새 장바구니
    data = []
    for q in questions:
        # 문제 하나를 {이름표: 내용} 모양으로 변신시켜요!
        data.append({"question": q.question, "choices": q.choices, "answer": q.answer})

    # 'quiz_data.json' 이라는 파일을 열어서 적어요 (w = write, 쓰기)
    with open("quiz_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("💾 문제가 성공적으로 저장되었어요!")

    # 5. 파일에서 문제들을 불러오는 함수
def load_questions():
    try:
        # 파일을 열어서 읽어요 (r = read, 읽기)
        with open("quiz_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        # 딕셔너리들을 다시 Quiz 객체로 변신!
        questions = []
        for item in data:
            questions.append(Quiz(item["question"], item["choices"], item["answer"]))
        return questions

    except FileNotFoundError:
        # 저장된 파일이 없으면 빈 장바구니를 돌려줘요
        print("📂 저장된 파일이 없어서 새로 시작해요!")
        return []

# 4. 메뉴 화면 함수
def main_menu():
    while True:
        print("\n--- 🎮 퀴즈 게임 메뉴 ---")
        print("1. 퀴즈 풀기")
        print("2. 문제 추가하기")
        print("3. 문제 수정하기")   # 👈 새로 추가!
        print("4. 종료")            # 👈 번호 바꿈! (3→4)
        
        choice = input("원하는 메뉴 번호를 입력하세요: ")

        if choice == '1':
            run_quiz(questions_list)
        elif choice == '2':
            add_question()
        elif choice == '3':              # 👈 새로 추가!
            edit_question()              # (이 함수는 곧 만들 거예요!)
        elif choice == '4':              # 👈 종료를 4로 변경!
            print("\n게임을 종료합니다. 다음에 또 만나요! 👋")
            break
        else:
            print("\n[경고] 1, 2, 3, 4 중에서만 골라주세요!")  # 👈 숫자 추가!
def add_question():
    print("\n--- 🆕 새로운 문제 추가 ---")
    question = input("문제 내용을 입력하세요: ")

    # 선택지 4개를 하나씩 입력받아요!
    choices = []
    for i in range(4):
        choice = input(f"{i + 1}번 선택지를 입력하세요: ")
        choices.append(choice)

    # 정답 번호를 입력받아요 (1~4)
    answer = int(input("정답 번호를 입력하세요 (1~4): "))

    # 새로운 Quiz 객체를 만들어서 리스트에 추가해요!
    new_q = Quiz(question, choices, answer)
    questions_list.append(new_q)
    save_questions(questions_list)
    print("\n[성공] 문제가 리스트에 추가되었습니다! ✅")
# 👇 이 아래에 새 함수를 붙여넣으세요!
def edit_question():
    if len(questions_list) == 0:
        print("\n[알림] 수정할 문제가 없어요! 먼저 문제를 추가해주세요!")
        return

    print("\n--- ✏️ 문제 수정하기 ---")
    for i in range(len(questions_list)):
        print(f"{i + 1}. {questions_list[i].text}")      # 👈 text로 수정!

    num = int(input("수정할 문제 번호를 입력하세요: "))

    new_q = input("새로운 문제 내용을 입력하세요: ")
    new_a = input("새로운 정답을 입력하세요: ")

    questions_list[num - 1].text = new_q       # 👈 text로 수정!
    questions_list[num - 1].answer = new_a

    save_questions(questions_list)
    print("[성공] 문제가 수정되었습니다! ✅")

# 5. 프로그램 시작점
if __name__ == "__main__":
    questions_list = load_questions()# 👈 이 줄 추가! (저장된 문제 불러오기)
    main_menu()
