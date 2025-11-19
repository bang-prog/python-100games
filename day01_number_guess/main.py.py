import random

def main(): 
    print("===数字当てゲーム===")
    answer = random.randint(1, 100)
    tries = 0 

    while True:
        guess_str = input("1から100の整数を入力してください(qで終了):")
        if guess_str == "q":
            print("ゲームを終了します。正解は", answer, "でした。")
            break

        #入力チェック
        if not guess_str.isdigit():
            print("数字を入力してください。")
            continue

        guess = int(guess_str)
        tries += 1

        if guess < answer:
            print("もっと大きいです。")
        elif guess > answer:
            print("もっと小さいです。")
        else:
            print("正解！", tries, "回で当てました！")
            break

if __name__ == "__main__":
    main()        


    