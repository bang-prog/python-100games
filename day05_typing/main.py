import random
import time

WORDS =["apple",
        "bananan",
        "orange",
        "grape",
        "melon",
        "peach",
        "lemon",
        "cherry",
        "strawberry",
        "watermelon",    
    ]

NUM_questions = 5

def main():
    print("タイピングゲームへようこそ！")
    print(f"英単語が{NUM_questions}個出てくるので、同じように入力してください。")
    print("終了するには q を押してください。")
    input("準備ができたら Enter キーを押してください。")

    correct = 0
    incorrect = 0
    total_time = 0.0

    for i in range(1, NUM_questions + 1):
        print(f"\n第{i}問目")

        word = random.choice(WORDS)
        print("単語：", word)

        start = time.time()
        user_input = input("入力：")
        end = time.time()

        if user_input == "q":
            print("ゲームを終了します。")
            break

        elapsed = end -start

        if user_input == word:
            print(f"正解！ {elapsed:.1f}秒かかりました。")
            correct += 1
            total_time += elapsed
        else:
            print(f"不正解！ 正しくは{word}です。")
            print(f"{elapsed:.1f}秒かかりました。")
            incorrect += 1

    print("\n=== 結果 ===")
    print(f"正解数：{correct} 不正解数：{incorrect}")

    if correct > 0:
        ave_time = total_time / correct
        print(f"正解平均タイム： {ave_time:.1f}秒")
    else:
        print("正解なしでした...次回頑張りましょう！")

if __name__ == "__main__":
    main()
