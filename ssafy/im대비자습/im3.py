for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    aready = []
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    for _ in range(m):
        xr, xc, l = map(int, input().split())
        if [xr, xc] not in aready:
            cnt += arr[xr][xc]
            aready.append([xr, xc])
        for i in range(4):
            for j in range(1, l+1):
                r = xr + dr[i]*j
                c = xc + dc[i]*j
                if 0 <= r < n and 0 <= c < n and [r, c] not in aready:
                    cnt += arr[r][c]
                    aready.append([r, c])
    print(f'#{t}', cnt)