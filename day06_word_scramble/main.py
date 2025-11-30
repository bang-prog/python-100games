import random
import time

WORDS = [
    "apple",
    "banana",
    "orange",
    "grape",
    "melon",
    "peach",
    "kiwi",
    "cherry",
    "strawberry",
    "watermelon",
]

NUM_questions = 5

def shuffle_word(word):
    letters = list(word) #letters == ["a", "p", "p", "l", "e"]
    while True:
        random.shuffle(letters)
        shuffled = "".join(letters) #"".join(["p", "a", "l", "p", "e"])
                                    #リストの中身を、間に「区切り文字」をはさみながら 1つの文字列にくっつける
        if shuffled != word:
            return shuffled
        
def main():
    print("=== DAY06: 単語並べ替えゲーム（Word Scramble） ===")
    print(f"英単語が {NUM_questions} 個出てきます。")
    print("バラバラになった文字から、元の単語を当ててください。")
    print("途中でやめたいときは q を入力して Enter。")
    input("準備ができたら Enter を押してください...")

    score = 0
    total_time = 0.0
    for i in range(1, NUM_questions + 1):
        print(f"\n第{i}問目")

        answer = random.choice(WORDS)
        scrambled = shuffle_word(answer)

        start = time.time()
        end = time.time()

        print("問題：", scrambled)
        user_input = input("答えを入力：")

        if user_input == "q":
            print("ゲームを終了します。")
            break

        elapsed = end - start

        if user_input == answer:
            print("正解！")
            score += 1
            total_time += elapsed
        else:
            print(f"不正解。正しい答えは {answer} です。")
    
    print("\n=== 結果 ===")
    print(f"正解数：{score}/{NUM_questions}")
    if score > 0:
        ave_time = total_time / NUM_questions
        print(f"平均正解時間は {ave_time} でした！")
    
    if score ==NUM_questions:
        print("パーフェクト！")
    elif score == 0:
        print("落ち着いて考えよう...")
    else:
        print("もうちょっと頑張ろう。")

if __name__ == "__main__":
    main()


            
        