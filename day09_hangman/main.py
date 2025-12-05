import random

WORDS = [
    "apple",
    "banana",
    "orange",
    "grape",
    "melon",
    "peach",
    "lemon",
    "cherry",
    "strawberry",
    "watermelon",
]

MAX_TRIES = 6

def main():
    print("=== 英単語当てゲームへようこそ！ ===")
    print("1文字ずつアルファベットを入力して、隠された英単語を当てよう。")
    print(f"単語の候補は[{','.join(WORDS)}]です。")
    print(f"間違えられるのは最大 {MAX_TRIES} 回です。")
    print("途中でやめたいときは q を入力して Enter。")
    input("準備ができたら Enter を押してください...")

    answer = random.choice(WORDS)
    guessed_letters = set()
    wrong_tries = 0

    def display_state():
        result = ""
        for ch in answer:
            if ch in guessed_letters:
                result += ch
            else:
                result += "_"
        print("現在の状態: " + " ".join(result))
        print(f"間違えた回数：{wrong_tries} / {MAX_TRIES}")
        print(f"入力した文字：{','.join(sorted(guessed_letters))}"if guessed_letters else "入力した文字：なし")

    while True:
        print("\n-----------------------------")
        display_state()

        if all(ch in guessed_letters for ch in answer):
            print("おめでとう！正解は{answer}でした！")
            break

        if wrong_tries >= MAX_TRIES:
            print(f"残念...正解は{answer}でした。")
            break

        user_input = input("1文字を入力してください (終了するには q): ").lower()

        if user_input == "q":
            print("ゲームを終了します。")
            break

        if len(user_input) != 1 or not user_input.isalpha():
            print("アルファベット1文字で入力してください。")
            continue
        if user_input in guessed_letters:
            print("その文字はすでに入力されています。別の文字を入力してください。")
            continue

        # 新しい文字として追加
        guessed_letters.add(user_input)

        if user_input in answer:
            print(f"{user_input}は単語に含まれています！")
        else:
            print(f"{user_input}は単語に含まれていません。")
            wrong_tries += 1

    print("ゲーム終了。遊んでくれてありがとう！")
    print("また遊んでみてね！")

if __name__ == "__main__":
    main()