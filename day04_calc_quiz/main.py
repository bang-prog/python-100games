import random
import time

NUM_QUESTIONS =5

def generate_question():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(["+", "-", "*"])

    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    else:
        answer = a * b

    question_text = f"{a} {op} {b} = ?"
    return question_text, answer

def main():
    print("四則演算クイズゲームへようこそ！")
    print(f"{NUM_QUESTIONS}問出題します！時間も計ります！")
    print("終了したいときは q を押してください")
    print("準備が出来たら Enter を押してください！")

    score = 0
    fscore = 0
    start_time = time.time()

    for i in range(1, NUM_QUESTIONS + 1):
        print(f"\n第 {i} 問目")
        question_text, answer = generate_question()
        print("問題", question_text)

        user_input = input("答えを整数で入力：")
        if user_input == "q":
            print("途中終了します")
            break

        if not user_input.lstrip("-").isdigit():
            print("整数を入力してください")
            continue

    user_answer = int(user_input)

    if user_answer == answer:
        print("正解！")
        score += 1
    else:
        print(f"不正解...正しい答えは {answer} でした！")
        fscore += 1

    end_time = time.time()
    elapsed = end_time - start_time

    print("===結果===")
    print(f"正解数： {score}問  不正解数： {fscore}問")
    print(f"かかった時間： {elapsed.if}秒")

if __name__ == "__main__":
    main()