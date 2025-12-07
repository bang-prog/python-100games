import random

NUMBER = 3
MAX_TRIES =10

def generateanswer():
    # かぶりなしのランダムな数字列を生成
    number = list("0123456789")
    random.shuffle(number)
    # 先頭は0にしない
    first = random.choice(number[1:]) # 0以外の数字から選ぶ
    remaining = []
    for n in number:
        if n != first:
            remaining.append(n)
    answer_list = [first]
    while len(answer_list) < NUMBER:
        n = random.choice(remaining)
        if n not in answer_list:
            answer_list.append(n)
    return "".join(answer_list)

def judge(answer: str, guess: str):
    #amswerとguessを比較して、hit or blowを返す
    hit = 0
    blow = 0

    for i in range(NUMBER):
        if guess[i] == answer[i]:
            hit += 1
        elif guess[i] in answer:
            blow += 1
    return hit, blow

def main():
    print("=== ヒット＆ブロー（3ケタ数字当て） ===")
    print(f"{NUMBER}ケタの、同じ数字を含まない数字を当ててください。")
    print(f"チャレンジ回数は最大 {MAX_TRIES} 回です。")
    print("例: 123, 507 など（先頭に0はありません）")
    print("途中でやめたいときは q を入力して Enter。")
    input("準備ができたら Enter を押してください...")

    answer = generateanswer()

    tries = 0

    while tries < MAX_TRIES:
        print("\n---------------------------")
        print(f"{tries + 1} 回目のチャレンジ")
        guess = input(f"{NUMBER}ケタの数字を入力: ")
        
        if guess == "q":
            print("ゲームを終了します。")
            return
        
        if len(guess) != NUMBER or not guess.isdigit() or len(set(guess)) != NUMBER or guess[0] == '0':
            print(f"{NUMBER}桁の数字で同じ数字が含まれないように入力してください（先頭に0は不可、かぶりなし）")
            continue

        tries += 1

        hit, blow = judge(answer, guess)
        print(f"結果: {hit} ヒット, {blow} ブロー")

        if hit == NUMBER:
            print(f"おめでとうございます！ {tries} 回で正解しました！")
            break
        else:
            print("まだ正解ではありません。")
    else:
        # 最大試行回数に達した場合
        print("\n回数オーバーです。正解は " + answer + " でした。")

    print("\n=== ゲーム終了 ===")
    print("また挑戦してくださいね！")

if __name__ == "__main__":
    main()
