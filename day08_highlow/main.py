import random

NUM_ROUNDS = 5

def main():
    print("=== High&Lowゲームへようこそ！===")
    print("1~13の数字がカードとして出ます。")
    print("次のカードが「今より High（大きい）」か「Low（小さい）」か当ててください。")
    print("h: High, l: Low, q: 終了")
    input("準備ができたら Enter を押してください...")

    score = 0

    for round_idx in range(1, NUM_ROUNDS + 1):
        print("--------------------------------")
        print(f"第{round_idx}回目")

        current = random.randint(1, 13)
        print(f"今のカード：{current}")

        choice = input("次のカードは (h)High か (l)Low か？ qで終了: ")
        if choice == "q":
            print("ゲームを終了します。")
            break

        if choice not in ("h", "l"):
            print("無効な入力です。h, l, q のいずれかを入力してください。")
            continue

        next_card = random.randint(1, 13)
        print(f"次のカード：{next_card}")

        if next_card == current:
            print("draw! 今回はノーカウント")
            continue

        higher = next_card > current

        if choice == "h" and higher:
            print("あなたの勝ち！")
            score += 1
        elif choice == "l" and not higher:
            print("あなたの勝ち！")
            score += 1
        else:
            print("あなたの負け！")

        print(f"現在のスコア：{score} / {round_idx}")

    print("\n=== ゲーム終了 ===")
    print(f"最終スコア: {score} / {NUM_ROUNDS}")

    if score == NUM_ROUNDS:
        print("パーフェクト！すごい！！✨")
    elif score == 0:
        print("全部はずれ… 次は頑張ろう。")
    else:
        print("いい感じ！ 運と勘が冴えてるね。")

if __name__ == "__main__":
    main()

