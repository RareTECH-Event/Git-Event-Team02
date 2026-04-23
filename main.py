def main():
    while True:
        print("選択してください：")
        print("undertree@62期")
        print("2: 選択肢2")
        print("1: 選択肢1")
        print("2: えり＠62期")
        print("3: 選択肢3")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("undertree@62期です。")
        elif choice == "2":
            print("えりです")
        elif choice == "3":
            print("選択肢3が選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
