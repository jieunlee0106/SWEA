for t in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    min_num = 10000

    for c in range(100):
        if ladder[0][c] == 1:
            cnt = 0
            for r in range(100):
                if c >= 0 and ladder[r][c+1] == 1:
                    while c > 0 and ladder[r][c+1] == 1:
                        c += 1
                        cnt += 1
                elif c =< 99 and ladder[r][c-1] == 1:
                    while c <= 99 and ladder[r][c-1] == 1:
                        c -= 1
                        cnt += 1
            if cnt <= min_num:
                min_num = cnt


# print(f'#{t+1}', real_result)