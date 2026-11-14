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