def main():
    while True:
        print("選択してください：")
        print("1: たか@59期")
        print("2: うっちー@58期")
        print("3: 選択肢3")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("たか@59期が選ばれました。")
        elif choice == "2":
            print("うっちー@58期が選ばれました。")
        elif choice == "3":
            print("選択肢3が選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()

