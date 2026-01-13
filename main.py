def main():
    while True:
        print("選択してください：")
        print("1: 生大をお願いします")
        print("2: otti")
        print("3: pon")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("生大が選ばれました。")
        elif choice == "2":
            print("otti")
        elif choice == "3":
            print("pon")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
