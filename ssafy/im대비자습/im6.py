for t in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    cnt = 0

    i = -1
    for r in range(n//2+1):
        i += 1
        for c in range((n//2)-i, (n//2)+i+1):
            cnt += arr[r][c]

    j = -1
    for r1 in range(n-1, n//2, -1):
        j += 1
        for c1 in range((n//2)-j, (n//2)+j+1):
            cnt += arr[r1][c1]

    print(f'#{t}', cnt)