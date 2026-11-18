import json
import os

# 데이터 파일은 이 파이썬 파일과 같은 폴더(프로젝트 루트)의 state.json 입니다.
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state.json")

LINE = "=" * 40
THIN_LINE = "-" * 40


# ---------------------------------------------------------------
# 1. Quiz 클래스: 퀴즈 "한 문제"를 표현하는 붕어빵 틀
# ---------------------------------------------------------------
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question  # 문제 내용
        self.choices = choices    # 선택지 4개 (리스트)
        self.answer = answer      # 정답 번호 (1~4)

    def show(self, number):
        """문제와 선택지를 화면에 보여줘요."""
        print(f"\n{THIN_LINE}")
        print(f"[문제 {number}]")
        print(self.question)
        print()
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def is_correct(self, user_answer):
        """사용자가 고른 번호가 정답이면 True."""
        return user_answer == self.answer

    def to_dict(self):
        """JSON에 저장할 수 있도록 딕셔너리로 바꿔요."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @staticmethod
    def from_dict(data):
        """딕셔너리를 Quiz 객체로 되돌려요. 모양이 이상하면 ValueError를 내요."""
        question = data["question"]
        choices = data["choices"]
        answer = data["answer"]

        if not isinstance(question, str) or not question.strip():
            raise ValueError("문제 내용이 올바르지 않아요.")
        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 4개여야 해요.")
        if not all(isinstance(c, str) and c.strip() for c in choices):
            raise ValueError("선택지 내용이 올바르지 않아요.")
        # bool은 int의 한 종류라서 따로 걸러내요.
        if not isinstance(answer, int) or isinstance(answer, bool) or not 1 <= answer <= 4:
            raise ValueError("정답 번호는 1~4여야 해요.")

        return Quiz(question, choices, answer)


# ---------------------------------------------------------------
# 2. 기본 퀴즈 데이터 (주제: 파이썬 기초) - 5개 이상!
#    다른 주제로 바꾸고 싶으면 이 부분만 고치면 돼요.
# ---------------------------------------------------------------
def make_default_quizzes():
    return [
        Quiz("Python을 만든 사람은?",
             ["Guido van Rossum", "Linus Torvalds", "Bjarne Stroustrup", "James Gosling"], 1),
        Quiz("파이썬에서 리스트를 만들 때 쓰는 기호는?",
             ["{ }", "[ ]", "( )", "< >"], 2),
        Quiz("화면에 글자를 출력하는 함수는?",
             ["input()", "print()", "len()", "type()"], 2),
        Quiz("'정수'를 나타내는 자료형 이름은?",
             ["str", "bool", "int", "dict"], 3),
        Quiz("'이름표(key): 값(value)' 형태로 데이터를 저장하는 자료형은?",
             ["list", "dict", "int", "bool"], 2),
        Quiz("조건에 따라 다른 동작을 하게 만드는 키워드는?",
             ["for", "def", "class", "if"], 4),
    ]


# ---------------------------------------------------------------
# 3. 입력 도우미 함수들 (공백 제거, 숫자 변환, 범위 검사, 빈 입력)
# ---------------------------------------------------------------
def read_text(prompt):
    """빈 입력이면 안내 후 다시 물어보는 글자 입력."""
    while True:
        text = input(prompt).strip()      # 앞뒤 공백 제거
        if text == "":
            print("⚠️ 빈 입력입니다. 내용을 입력하세요.")
            continue
        return text


def read_text_or_keep(prompt, current):
    """수정할 때 쓰는 입력: 그냥 Enter를 누르면 기존 값을 그대로 유지해요."""
    text = input(prompt).strip()
    if text == "":
        return current
    return text


def read_int_or_keep(prompt, low, high, current):
    """수정할 때 쓰는 숫자 입력: Enter는 기존 값 유지, 숫자가 이상하면 다시 입력."""
    while True:
        text = input(prompt).strip()
        if text == "":
            return current
        try:
            number = int(text)
        except ValueError:
            print(f"⚠️ 잘못된 입력입니다. {low}-{high} 사이의 숫자를 입력하세요.")
            continue
        if number < low or number > high:
            print(f"⚠️ 잘못된 입력입니다. {low}-{high} 사이의 숫자를 입력하세요.")
            continue
        return number


def read_int(prompt, low, high):
    """low~high 사이의 숫자를 올바르게 입력할 때까지 반복해서 물어봐요."""
    while True:
        text = input(prompt).strip()      # 앞뒤 공백 제거 (예: " 1 " -> "1")
        if text == "":
            print(f"⚠️ 빈 입력입니다. {low}-{high} 사이의 숫자를 입력하세요.")
            continue
        try:
            number = int(text)
        except ValueError:                # "abc" 같은 입력
            print(f"⚠️ 잘못된 입력입니다. {low}-{high} 사이의 숫자를 입력하세요.")
            continue
        if number < low or number > high:  # 범위 밖 (예: 9, 0)
            print(f"⚠️ 잘못된 입력입니다. {low}-{high} 사이의 숫자를 입력하세요.")
            continue
        return number


# ---------------------------------------------------------------
# 4. QuizGame 클래스: 게임 전체를 관리해요
# ---------------------------------------------------------------
class QuizGame:
    def __init__(self):
        self.quizzes = []        # 퀴즈 목록
        self.best_score = None   # 최고 점수 (아직 안 풀었으면 None)

    # ----- 파일 저장 / 불러오기 -----
    def save_state(self):
        """퀴즈와 최고 점수를 state.json에 저장해요."""
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }
        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except OSError as e:
            print(f"⚠️ 저장 중 오류가 발생했어요: {e}")
            return False
        return True

    def load_state(self):
        """state.json을 불러와요. 없거나 손상되면 기본 데이터를 사용해요."""
        if not os.path.exists(STATE_FILE):
            print("📂 저장된 파일이 없어서 기본 퀴즈로 시작해요!")
            self.reset_to_default()
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            quizzes = [Quiz.from_dict(item) for item in data["quizzes"]]
            best_score = data["best_score"]
            if best_score is not None and (
                not isinstance(best_score, int) or isinstance(best_score, bool)
            ):
                raise ValueError("최고 점수 형식이 올바르지 않아요.")

            self.quizzes = quizzes
            self.best_score = best_score
            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, "
                  f"{self.best_score_text()})")
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
            # 파일이 깨졌거나 읽을 수 없는 경우: 안내 후 기본 데이터로 복구
            print("⚠️ 저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            self.reset_to_default()

    def reset_to_default(self):
        self.quizzes = make_default_quizzes()
        self.best_score = None
        self.save_state()

    def best_score_text(self):
        if self.best_score is None:
            return "최고점수 없음"
        return f"최고점수 {self.best_score}점"

    # ----- 메뉴 -----
    def show_menu(self):
        print(f"\n{LINE}")
        print("        🎯 나만의 퀴즈 게임 🎯")
        print(LINE)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 퀴즈 수정")
        print("6. 종료")
        print(LINE)

    # ----- 1. 퀴즈 풀기 -----
    def play_quiz(self):
        if len(self.quizzes) == 0:
            print("\n⚠️ 등록된 퀴즈가 없어요. 먼저 퀴즈를 추가해 주세요!")
            return

        total = len(self.quizzes)
        correct = 0
        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")

        for number, quiz in enumerate(self.quizzes, start=1):
            quiz.show(number)
            user_answer = read_int("\n정답 입력: ", 1, 4)
            if quiz.is_correct(user_answer):
                print("✅ 정답입니다!")
                correct += 1
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")

        score = correct * 100 // total   # 100점 만점으로 계산
        print(f"\n{LINE}")
        print(f"🏆 결과: {total}문제 중 {correct}문제 정답! ({score}점)")

        # 최고 점수와 비교해서 갱신
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
            self.save_state()
        print(LINE)

    # ----- 2. 퀴즈 추가 -----
    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")
        question = read_text("문제를 입력하세요: ")

        choices = []
        for i in range(1, 5):
            choices.append(read_text(f"선택지 {i}: "))

        answer = read_int("정답 번호 (1-4): ", 1, 4)

        self.quizzes.append(Quiz(question, choices, answer))
        if self.save_state():
            print("\n✅ 퀴즈가 추가되었습니다!")

    # ----- 3. 퀴즈 목록 -----
    def show_quiz_list(self):
        if len(self.quizzes) == 0:
            print("\n⚠️ 등록된 퀴즈가 없어요.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print(THIN_LINE)
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")
        print(THIN_LINE)

    # ----- 4. 점수 확인 -----
    def show_best_score(self):
        if self.best_score is None:
            print("\n⚠️ 아직 퀴즈를 풀지 않았어요. 먼저 퀴즈를 풀어보세요!")
        else:
            print(f"\n🏆 최고 점수: {self.best_score}점")

    # ----- 5. 퀴즈 수정 -----
    def edit_quiz(self):
        if len(self.quizzes) == 0:
            print("\n⚠️ 수정할 퀴즈가 없어요. 먼저 퀴즈를 추가해 주세요!")
            return

        self.show_quiz_list()
        number = read_int("수정할 퀴즈 번호: ", 1, len(self.quizzes))
        quiz = self.quizzes[number - 1]

        print(f"\n✏️ {number}번 퀴즈를 수정합니다. (그냥 Enter를 누르면 기존 값 유지)")

        # 새 값을 모두 입력받은 뒤에 한꺼번에 반영해요. (중간에 중단돼도 안전)
        new_question = read_text_or_keep(f"문제 [{quiz.question}]: ", quiz.question)

        new_choices = []
        for i, old_choice in enumerate(quiz.choices, start=1):
            new_choices.append(read_text_or_keep(f"선택지 {i} [{old_choice}]: ", old_choice))

        new_answer = read_int_or_keep(
            f"정답 번호 (1-4) [{quiz.answer}]: ", 1, 4, quiz.answer
        )

        quiz.question = new_question
        quiz.choices = new_choices
        quiz.answer = new_answer

        if self.save_state():
            print("\n✅ 퀴즈가 수정되었습니다!")

    # ----- 프로그램 실행 -----
    def run(self):
        self.load_state()
        try:
            while True:
                self.show_menu()
                choice = read_int("선택: ", 1, 6)

                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_quiz_list()
                elif choice == 4:
                    self.show_best_score()
                elif choice == 5:
                    self.edit_quiz()
                elif choice == 6:
                    self.save_state()
                    print("\n게임을 종료합니다. 다음에 또 만나요! 👋")
                    break
        except (KeyboardInterrupt, EOFError):
            # Ctrl+C 또는 입력 스트림 종료: 에러로 죽지 않고 저장 후 안전하게 종료
            print("\n\n⚠️ 입력이 중단되었습니다. 데이터를 저장하고 종료합니다.")
            self.save_state()
            print("안전하게 종료되었습니다. 👋")


# ---------------------------------------------------------------
# 5. 프로그램 시작점
# ---------------------------------------------------------------
if __name__ == "__main__":
    game = QuizGame()
    game.run()