import random

PLAYER_MAX_HP = 30
ENEMY_MAX_HP = 20

def main():
    print("===バトルゲームへようこそ===")
    print("あなた vs モンスターのHPバトル！")
    print("= コマンド一覧 = \n1.攻撃 \n2.防御 \n3.回復 \nq.終了" )
    input("準備ができたら Enter を押してください...")

    player_hp = PLAYER_MAX_HP
    enemy_hp = ENEMY_MAX_HP

    turn = 1

    while player_hp > enemy_hp > 0:
        print("\n------------------------")
        print(f"ターン{turn}")
        print(f"あなたのHP：{player_hp} / {PLAYER_MAX_HP}")
        print(f"モンスターのHP：{enemy_hp} / {ENEMY_MAX_HP}")

        command = input("コマンドを選択(1.攻撃 2.防御 3.回復 q.終了): ")

        if command == 'q':
            print("あなたは戦いを放棄した...ゲーム終了")
            return
        
        # プレイヤーのターン
        if command == '1':
            damage = random.randint(4, 10)
            print(f"あなたは攻撃した！モンスターに{damage}ダメージ！")
            enemy_hp -= damage
            if enemy_hp < 0:
                print("モンスターを倒した！あなたの勝利！")
                break
        elif command == '2':
            print("あなたは防御した！次の攻撃のダメージを半減する！")
            player_hp -= damage //2
            continue
        elif command == '3':
            heal = random.randint(4, 8)
            player_hp += heal
            if player_hp > PLAYER_MAX_HP:
                player_hp = PLAYER_MAX_HP
            print(f"あなたは回復した！{heal}回復！ 現在のHP: {player_hp}")
        else:
            print("無効なコマンドです。ターンを無駄にしてしまった...")

        # モンスターのターン
        if enemy_hp > 0:
            enemy_damage = random.randint(4, 9)
            print(f"モンスターの攻撃！あなたに{enemy_damage}ダメージ！")
            player_hp -= enemy_damage
            if player_hp <= 0:
                print("あなたは倒れた...ゲームオーバー")
                break
        
        turn += 1
    
    print("\n===ゲーム終了===")
    print(f"==最終結果== \nあなたのHP: {max(player_hp, 0)}, モンスターのHP: {max(enemy_hp, 0)}")

if __name__ == "__main__":
    main()
