def eat_apple(x_player, y_player, x_apple, y_apple):
    x1_player, y1_player, w_player, h_player = x_player, y_player, 10, 10
    x2_player = x1_player + w_player
    y2_player = y1_player + h_player

    x1_apple, y1_apple, w_apple, h_apple = x_apple, y_apple, 10, 10
    x2_apple = x1_apple + w_apple
    y2_apple = y1_apple + h_apple

    s1 = (x1_player >= x1_apple and x1_player <= x2_apple) or (x2_player >= x1_apple and x2_player <= x2_apple)
    s2 = (y1_player >= y1_apple and y1_player <= y2_apple) or (y2_player >= y1_apple and y2_player <= y2_apple)
    s3 = (x1_apple >= x1_player and x1_apple <= x2_player) or (x2_apple >= x1_player and x2_apple <= x2_player)
    s4 = (y1_apple >= y1_player and y1_apple <= y2_player) or (y2_apple >= y1_player and y2_apple <= y2_player)

    if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)):
        return True
    return False

eat_apple(20, 20, 10, 10)