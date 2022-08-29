for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = 0
            for r in range(i, i+m):
                for c in range(j, j+m):
                    cnt += arr[r][c]
            if cnt > max_cnt:
                max_cnt = cnt
    print(f'#{t}', max_cnt)