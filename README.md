# Mission 2 시작

# 🎮 미션 2: 나만의 퀴즈 게임 만들기

## 1. 이번 미션은 무엇을 하는 건가요? 🚀
한마디로 말하면 **"파이썬으로 똑똑한 퀴즈 박사님 만들기"**예요. 
단순히 문제를 푸는 것뿐만 아니라, 내가 문제를 직접 추가할 수도 있고, 게임을 껐다 켜도 내 점수를 기억하는 아주 똑똑한 프로그램을 만드는 것이 목표예요.

---

## 2. 우리가 배워야 할 핵심 개념 💡

*   **① 클래스 (Class) : "붕어빵 틀"**
    *   **설명:** 퀴즈 하나하나를 만들 때마다 똑같은 코드를 계속 쓰면 힘들겠죠? 그래서 '퀴즈'라는 틀을 하나 만들어두는 거예요.
    *   **역할:** 이 틀에는 '문제', '보기 4개', '정답 번호'가 들어갈 자리가 미리 정해져 있어요.

*   **② JSON (제이슨) : "비밀 일기장"**
    *   **설명:** 컴퓨터는 게임을 끄면 모든 걸 까먹어요. 그래서 게임을 끄기 전에 JSON이라는 일기장에 기록을 남겨요.
    *   **역할:** 다음에 게임을 켤 때 이 일기장을 읽어서 예전 점수와 문제를 다시 불러와요.

*   **③ 예외 처리 (Try/Except) : "실수 방패"**
    *   **설명:** 숫자를 입력해야 하는데 문자를 입력하면 프로그램이 멈춰버려요. 이때 "당황하지 마! 다시 입력해줘"라고 알려주는 방패예요.

*   **④ Git 브랜치 (Branch) : "평행 우주"**
    *   **설명:** 원래 만들던 게임을 망치지 않게 복사본 우주를 만들어 거기서 새로운 기능을 테스트해요. 잘 되면 나중에 합쳐요!

---

## 3. 미션 성공을 위해 해야 할 일들 📝

1.  **메뉴 만들기**: 사용자가 번호를 골라 기능을 선택하는 화면을 만들어요.
2.  **퀴즈 틀(클래스) 만들기**: 문제와 정답을 담을 수 있는 주머니를 만들어요.
3.  **저장 기능 만들기**: 점수와 문제를 `state.json` 파일에 저장하고 불러와요.
4.  **Git으로 기록하기**: 기능을 만들 때마다 깃허브에 도장을 찍어요. (최소 10번 이상!)
5.  **설명서 작성**: 이 게임이 어떤 게임인지 멋지게 적어주면 끝!

## 💡 코드 설명 (학생을 위한 팁!)
1.  while True:: 이 코드는 "내가 그만하라고 할 때까지 계속 반복해!"라는 뜻이에요. 덕분에 메뉴가 한 번 나오고 끝나는 게 아니라 계속 나타나게 됩니다.
2.  input(): 사용자가 키보드로 입력한 값을 받아오는 함수예요.
3.  break: 3번을 눌렀을 때 while 반복문을 멈추고 게임을 끝내주는 아주 중요한 역할을 해요.

```
def main_menu():
    while True:
        print("\n--- 🎮 퀴즈 게임 메뉴 ---")
        print("1. 퀴즈 풀기")
        print("2. 문제 추가하기")
        print("3. 종료")
        
        choice = input("원하는 메뉴 번호를 입력하세요: ")

        if choice == '1':
            print("\n[알림] 아직 퀴즈 기능이 준비되지 않았어요!")
        elif choice == '2':
            print("\n[알림] 아직 문제 추가 기능이 준비되지 않았어요!")
        elif choice == '3':
            print("\n게임을 종료합니다. 다음에 또 만나요! 👋")
            break  # 반복문을 빠져나가서 프로그램을 종료해요.
        else:
            print("\n[경고] 1, 2, 3 중에서만 골라주세요!")

# 이 프로그램이 실행될 때 main_menu 함수를 실행시켜요.
if __name__ == "__main__":
    main_menu()
```

## 💡 코드 설명
```
# 1. 퀴즈 문제의 틀(클래스)을 만들어요.
class Question:
    def __init__(self, text, answer):
        self.text = text      # 문제 내용
        self.answer = answer  # 정답

# --- 기존 코드 (main_menu 함수 등) ---
def main_menu():
    # ... (생략)
    
```
1.  class Question:: 이제부터 Question이라는 이름의 붕어빵 틀을 만들겠다는 뜻이에요.
2.  __init__: 붕어빵을 처음 구울 때(객체를 만들 때) 문제 내용과 정답을 넣어서 초기화해주는 특수한 함수예요.
3.  self.text, self.answer: 각 문제마다 자기만의 질문과 답을 저장하는 저장 공간이에요.

## 💡 팁
1.  파이썬은 들여쓰기로 "이 코드가 함수 안에 포함된 건지 아닌지"를 구별해요.
2.  def, if, while 처럼 끝에 콜론(:)이 붙는 문장 바로 다음 줄은 무조건 들여쓰기를 해야 한다고 기억하면 쉬워요!

```
def main_menu():
    # 여기서부터는 Tab을 눌러서 안으로 들여써야 해요!
    while True:
        print("\n--- 🎮 퀴즈 게임 메뉴 ---")
        print("1. 퀴즈 풀기")
        print("2. 문제 추가하기")
        print("3. 종료")
        
        choice = input("원하는 메뉴 번호를 입력하세요: ")

        if choice == '1':
            print("\n[알림] 아직 퀴즈 기능이 준비되지 않았어요!")
        elif choice == '2':
            print("\n[알림] 아직 문제 추가 기능이 준비되지 않았어요!")
        elif choice == '3':
            print("\n게임을 종료합니다. 다음에 또 만나요! 👋")
            break
        else:
            print("\n[경고] 1, 2, 3 중에서만 골라주세요!")

# 함수가 끝났으므로 여기는 다시 맨 앞으로 붙여서 써요 (들여쓰기 X)
if __name__ == "__main__":
    main_menu()
```

## 💡 요약하자면?
1.  class와 def: "이런 도구를 만들 거야"라고 미리 알려주는 부분 (위쪽)
2.  if __name__ == "__main__":: "이제 진짜 시작해!"라고 버튼을 누르는 부분 (맨 아래쪽)

```
# 1. 클래스 정의 (붕어빵 틀)
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

# 2. 함수 정의 (기능 설명)
def main_menu():
    while True:
        print("\n--- 🎮 퀴즈 게임 메뉴 ---")
        print("1. 퀴즈 풀기")
        print("2. 문제 추가하기")
        print("3. 종료")
        
        choice = input("원하는 메뉴 번호를 입력하세요: ")

        if choice == '1':
            print("\n[알림] 아직 퀴즈 기능이 준비되지 않았어요!")
        elif choice == '2':
            print("\n[알림] 아직 문제 추가 기능이 준비되지 않았어요!")
        elif choice == '3':
            print("\n게임을 종료합니다. 다음에 또 만나요! 👋")
            break
        else:
            print("\n[경고] 1, 2, 3 중에서만 골라주세요!")

# 3. 실제 실행 (맨 마지막에!)
if __name__ == "__main__":
    main_menu()

```

## 🛠️ 3단계: 진짜 퀴즈 문제 만들고 풀기
이제 메뉴만 있는 껍데기에서 벗어나, 진짜 퀴즈를 풀 수 있게 만들어볼까요?

1.  퀴즈 문제 리스트 만들기
main_menu() 함수 바로 위에, 우리가 만든 Question 클래스를 사용해서 문제 리스트를 만들어줍니다.

2.  퀴즈 풀기 함수(run_quiz) 만들기
문제를 하나씩 보여주고 정답을 맞혔는지 확인하는 기능을 만들 거예요.

quiz_game.py 파일을 아래와 같이 업데이트해 보세요. (기존 코드를 참고해서 추가/수정하시면 됩니다!)

```
# ... (Question 클래스는 그대로 두세요)

# 1. 퀴즈 문제들을 리스트에 담아둡니다.
questions_list = [
    Question("대한민국의 수도는?", "서울"),
    Question("파이썬을 만든 사람은 귀도 반 ( )?", "로섬"),
    Question("사과를 영어로 하면?", "apple")
]

# 2. 퀴즈를 진행하는 함수를 만들어요.
def run_quiz(questions):
    score = 0
    print(f"\n총 {len(questions)}문제를 시작합니다!")
    
    for q in questions:
        answer = input(f"{q.text} 정답 입력: ")
        if answer.strip() == q.answer:  # strip()은 양쪽 공백을 제거해줘요
            print("정답입니다! ✨")
            score += 1
        else:
            print(f"아쉽네요. 정답은 '{q.answer}'입니다. 😢")
            
    print(f"\n--- 퀴즈 종료! ---")
    print(f"당신의 점수: {score} / {len(questions)}")

# 3. main_menu 함수에서 1번을 눌렀을 때 run_quiz를 실행하게 수정해요.
def main_menu():
    while True:
        # ... (메뉴 출력 부분 생략)
        choice = input("원하는 메뉴 번호를 입력하세요: ")

        if choice == '1':
            run_quiz(questions_list)  # 퀴즈 시작!
        elif choice == '2':
            print("\n[알림] 아직 문제 추가 기능은 준비 중이에요!")
        # ... (나머지 동일)

```

## 💡 무엇이 달라졌나요?
1.   questions_list 추가: 퀴즈 문제 3개를 미리 만들어 두었습니다.
2.   run_quiz 함수 추가: 문제를 하나씩 보여주고, 사용자의 입력을 받아 정답인지 확인하는 '진짜 게임 로직'이 들어갔어요.
3.   순서 정리: 파이썬은 위에서 아래로 읽기 때문에, 도구(함수)를 먼저 정의하고 **마지막에 실행(main_menu)**하도록 순서를 맞췄습니다.

```
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
            print("\n[알림] 아직 문제 추가 기능은 준비 중이에요!")
        elif choice == '3':
            print("\n게임을 종료합니다. 다음에 또 만나요! 👋")
            break
        else:
            print("\n[경고] 1, 2, 3 중에서만 골라주세요!")

# 5. 프로그램 시작점
if __name__ == "__main__":
    main_menu()
```

## 🛠️ 4단계: 문제 추가 기능 만들기
run_quiz 함수 아래에 새로운 문제를 리스트에 추가하는 add_question 함수를 만들어 봅시다.

1. add_question 함수 추가하기
->run_quiz 함수가 끝나는 지점 다음에 아래 코드를 넣어주세요.

```
def add_question():
    print("\n--- ➕ 새로운 문제 추가 ---")
    text = input("문제 내용을 입력하세요: ")
    answer = input("정답을 입력하세요: ")
    
    # 새로운 Question 객체를 만들어서 리스트에 추가(append)해요!
    new_q = Question(text, answer)
    questions_list.append(new_q)
    
    print("\n[성공] 문제가 리스트에 추가되었습니다! ✅")
```

2. main_menu에서 2번 선택 시 연결하기
기존에 print("[알림] 아직 준비 중...")이었던 부분을 방금 만든 함수로 바꿔줍니다.

```
        elif choice == '2':
            add_question()  # 문제 추가 함수 실행!
```

💡 여기서 잠깐! (중요한 개념)
questions_list.append(new_q): append는 리스트의 맨 뒤에 새로운 데이터를 붙이는 명령어예요. 마치 기차 뒤에 새로운 칸을 하나 더 연결하는 것과 같죠! 🚂


## 아하, 이 에러는 파이썬에서 가장 자주 만나는 '들여쓰기(Indentation)' 문제예요! 😅

사진을 자세히 보니 elif choice == '3': 부분과 그 아래 else: 부분이 앞으로 너무 많이 들어가 있거나, 줄이 맞지 않아서 발생한 에러입니다. 파이썬은 줄 맞추기에 아주 예민하거든요.

🛠️ 해결 방법
main_menu 함수 안의 if-elif-else 줄을 똑같이 맞춰줘야 합니다. 아래 그림처럼 if, elif, else가 수직으로 딱 맞아야 해요.

[수정 전 (현재 상태)]
```
        if choice == '1':
            run_quiz(questions_list)
        elif choice == '2':
            add_question()
          elif choice == '3':  # 👈 여기가 더 들어가 있거나 줄이 안 맞아요!
              break
            else:              # 👈 여기도 줄이 안 맞아요!
```

[수정 후 (이렇게 맞춰주세요!)]
```
        if choice == '1':
            run_quiz(questions_list)
        elif choice == '2':
            add_question()
        elif choice == '3':  # 👈 if, elif 들과 세로줄을 똑같이!
            print("\n게임을 종료합니다. 다음에 또 만나요! 👋")
            break
        else:                # 👈 여기도 세로줄을 똑같이!
            print("\n[경고] 1, 2, 3 중에서만 골라주세요!")
```