for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [[0]*n for _ in range(n)]

    if n == 4:
        arr[1][2], arr[2][1], arr[1][1], arr[2][2] = 1, 1, 2, 2
    elif n == 6:
        arr[3][2], arr[2][3], arr[2][2], arr[3][3] = 1, 1, 2, 2
    elif n == 8:
        arr[3][4], arr[4][3], arr[4][4], arr[3][3] = 1, 1, 2, 2

    for game in range(m):
        x, y, player = map(int, input().split())
        x -= 1
        y -= 1
        arr[y][x] = player

        if player == 1:
            other = 2
        elif player == 2:
            other = 1
        d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        for ii in range(8):
            for g in range(1, n):

                X = x + d[ii][1]*g
                Y = y + d[ii][0]*g

                if 0 <= X < n and 0 <= Y < n and arr[Y][X] == 0:
                    break

                elif 0 <= X < n and 0 <= Y < n and arr[Y][X] == player:
                    for gg in range(1, g):
                        X2 = x + d[ii][1]*gg
                        Y2 = y + d[ii][0]*gg
                        arr[Y2][X2] = player
                    break       # 중요
                else:
                    continue


    black = 0
    white = 0
    for a in range(n):
        for b in range(n):
            if arr[a][b] == 1:
                black += 1
            elif arr[a][b] == 2:
                white += 1
    print(f'#{t}', black, white)