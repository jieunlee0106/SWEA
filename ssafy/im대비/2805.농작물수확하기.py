for t in range(1, int(input()+1)):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    m = n//2
    arr_r, arr_c = m, m

    j = 0
    sum_list = []
    for r in range(n):
        for c in range(n):
            sum_list += arr[r][c]