for t in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    start = []

    cnt_list = []
    for c in range(100):
        if ladder[0][c] == 1:
            cnt = 0
            for r in range(1, 101):
                if c > 0 and ladder[r][c+1] == 1:
                    while c > 0 and ladder[r][c+1] == 1:
                        c += 1
                        cnt += 1

                elif c < 100 and ladder[r][c-1] == 1:
                    while c < 100 and ladder[r][c-1] == 1:
                        c -= 1
                        cnt += 1
            cnt_list.append(cnt)

    result = cnt_list.index(min(cnt_list))
    cnt_il = -1
    for i in range(100):
       if ladder[0][i] == 1:
            cnt_il += 1
            if cnt_il == 3:
                real_result = i



print(f'#{t+1}', real_result)