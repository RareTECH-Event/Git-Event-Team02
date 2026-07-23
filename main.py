def main():
    while True:
        print("選択してください：")
        print("1: ぴょんす")
        print("2: Shinya")
        print("3: tagpyon")
        print("4: 選択肢4")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("ぴょんす")
        elif choice == "2":
            print("Shinyaが選ばれました。")
        elif choice == "3":
            print("tagpyonが選ばれました。")
        elif choice == "4":
            print("選択肢4が選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")


if __name__ == "__main__":
    main()
