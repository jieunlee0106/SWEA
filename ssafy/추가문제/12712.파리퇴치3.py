for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    def fly(r, c, m):
        srr = 0
        for i in range(r-2, r+3):
            for j in range(c-2, c+2):
                srr += arr[i][j]
        return srr
    def fly2(r, c, m):
        srr2 = 0
        for i in range(r-2, r+3):
            for j in range(c-2, c+3):
                srr2 += arr[i][j]
        return srr2

    ans = 0
    for r in range(n):
        for c in range(n):
            if r-m > 0 and r+m < n and c-m > 0 and c+m < n:
                srr = fly(r, c, m)
                srr2 = fly(r, c, m)
                if  srr >= srr2:
                    if srr > ans:
                        ans = srr
                elif srr < srr2:
                    if srr2 > ans:
                        ans = srr2
    print(ans)