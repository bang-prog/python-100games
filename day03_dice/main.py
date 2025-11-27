import random

NUM_ROUNDS = 5 #何回勝負するか

def main():
    print("サイコロゲームへようこそ！")
    print(f"{NUM_ROUNDS}回勝負です。Enterでサイコロを振ります。(qで終了)")

    win = 0
    lose = 0
    draw = 0

    for round_idx in range(1, NUM_ROUNDS + 1):
        cmd = input(f"\n回目：Enterでサイコロを振る（qで終了）")

        if cmd == "q":
            print("ゲームを終了します。")
            break

        player = random.randint(1, 6)
        cpu = random.randint(1, 6)

        print(f"あなたの出目：{player}")
        print(f"コンピュータの出目：{cpu}")

        if player > cpu:
            print("あなたの勝ち！")
            win += 1
        elif player < cpu:
            print("あなたの負け ^_^")
            lose += 1
        else:
            print("draw -_-")
            draw += 1

        print(f"現在の戦績：{win}勝 {lose}敗 {draw}分")
        print("-"*30)

    print("===最終結果===")
    print(f"{win}勝 {lose}敗 {draw}分")

    if win > lose:
        print("あなたの勝ち！")
    elif win < lose:
        print("あなたの負け ^_^")
    else:
        print("引き分け -_-")

if __name__ == "__main__":
    main()
