def check_decision(coordinate_map):
    decision_coordinates = [7, 56, 448, 73, 146, 292, 273, 84]

    #判定処理
    total_val = sum([int(i)for i in coordinate_map])
    if total_val in decision_coordinates:
        return True
    return False

def marubatu_game():
    print('以下の座標を選択してください')
    text = """
     1|2|3
     -----
     4|5|6
     -----
     7|8|9
     """
    print(text)
    coordinate_list = [str(i) for i in range(1, 10)]
    coordinate = [2**i for i in range(9)]

   # print('candidates : ')
   # print(candidates)
   # print(coordinate_list)

    pre_user_input = str()
    #画像のエラー箇所
    pre_user_operations = []

    pos_user_input = str()
    pos_user_operations = []

    err_message = '正しい座標を入力してください'
   
    turn_user = 0
    turn_count = 0

    while True:
        if turn_user == 0:
            try:
                mes = 'pre_userの座標を入力'
                pre_user_input = input(mes)
            except Exception as e:
                print('err_message')
                continue
            if pre_user_input in coordinate_list:
                text = text.replace(str(pos_user_input), ('x'))
                idx = coordinate_list.index(pos_user_input)
                coordinate_list[idx] = 'x'
                pos_user_operations.append(candidates)[idx]
                print(text)
                if check_decision(pre_user_operations):
                    print('user0の勝ち')
                    break
            else:
                print(err_message)
                continue
            turn_user = 1
            turn_count += 1
        else:
            try:
                mes = 'pos_userの座標を入力'
                pos_user_input = input(mes)
            except Exception as e:
                print(err_message)
                continue
            if pos_user_input in coordinate_list:
                text = text.replace(str(pos_user_input), "x")
                idx = coordinate_list.index(pos_user_input)
                coordinate_list[idx] = 'x'
                pos_user_operations.append(candidates[idx])
                print(text)
                if check_decision(pos_user_operations):
                    print('user1の勝ち')
                    break
            else:
                print(err_message)
                continue
            turn_user = 0
            turn_count += 1
        if turn_count == 9:
            print('引き分けです')
            break

marubatu_game()