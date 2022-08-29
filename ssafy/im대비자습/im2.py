for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    slist= []
    for _ in range(m):
        ru, cu, l = map(int, input().split())
        for r in range(ru, ru+l):
            for c in range(cu, cu+l):
                if 0 <= r < n and 0 <= c < n and [r, c] not in slist:
                    cnt += arr[r][c]
                    slist.append([r, c])
    print(f'#{t}', cnt)