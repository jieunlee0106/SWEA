T = int(input())
for t in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    a = [[0]*n for _ in range(n)]
    b = [[0]*n for _ in range(n)]
    d = [[0]*n for _ in range(n)]
    # 90
    for r in range(n):
        for c in range(n):
            a[r][c] = arr[n-c-1][r]
            b[r][c] = arr[n-r-1][n-c-1]
            d[r][c] = arr[c][n-r-1]

    print(f'#{t+1}')

    for i in range(n):
        for e in range(n):
            print(a[i][e], end='')
        print(end=' ')
        for f in range(n):
            print(b[i][f], end='')
        print(end=' ')
        for g in range(n):
            print(d[i][g], end='')
        print()