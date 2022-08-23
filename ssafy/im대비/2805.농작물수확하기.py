for t in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    m = n//2
    arr_r, arr_c = m, m
    i = 0
    sum_n = 0
    for r in range(m, -1, -1):
        for c in range(i, n-i):
            sum_n += arr[r][c]
        i += 1
    i = 1
    for r in range(m+1, n):
        for c in range(i, n-i):
            sum_n += arr[r][c]
        i += 1
    print(f'#{t}', sum_n)