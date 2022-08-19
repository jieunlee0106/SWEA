T = int(input())

for t in range(T):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    c_total_cnt = 0
    for r in range(n):
        cnt = 0
        for c in range(n):
            if puzzle[r][c] == 1:
                cnt += 1
                if cnt == k:
                    c_total_cnt += 1
                elif cnt == k + 1:
                    c_total_cnt -= 1
            else:
                cnt = 0
    r_total_cnt = 0
    for c in range(n):
        cnt = 0
        for r in range(n):
            if puzzle[r][c] == 1:
                cnt += 1
                if cnt == k:
                    r_total_cnt += 1
                elif cnt == k + 1:
                    r_total_cnt -= 1
            else:
                cnt = 0
    total_cnt = r_total_cnt + c_total_cnt
    print(f'#{t + 1}', total_cnt)