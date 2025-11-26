import random

HANDS = ["グー", "チョキ", "パー"]

def judge(plyer, cpu):
    "勝敗を判定する関数"
    if plyer == cpu:
        return "あいこ"
    
    if(
        (plyer == "グー" and cpu == "チョキ") or
        (plyer == "チョキ" and cpu == "パー") or
        (plyer == "パー" and cpu == "グー") 
        
    ):
        return "あなたの勝ち"
    else:
        return "あなたの負け"

def main():
    print("じゃんけんゲーム！")
    print("グー、チョキ、パーのいずれかを入力してください (qで終了)")

    win = 0
    lose = 0
    draw = 0

    while True:
        hand = input("あなたの手：")

        if hand == "q":
            print("ゲームを終了します")
            break

        if hand not in HANDS:
            print("グー、チョキ、パーのいずれかを入力してください")
            continue

        cpu_hand = random.choice(HANDS)
        print(f"コンピュータの手: {cpu_hand}")


        result = judge(hand, cpu_hand)

        if result == "あなたの勝ち":
            print("あなたの勝ち")
            win += 1
        elif result == "あなたの負け":
            print("あなたの負け")
            lose += 1
        else:
            print("あいこ")
            draw += 1
        
        print(f"現在の戦績: {win}勝 {lose}敗 {draw}分")
        print("-" * 30)
    
    print("最終戦績：", win, "勝", lose, "敗", draw, "分でした！")

if __name__ == "__main__":
    main()
