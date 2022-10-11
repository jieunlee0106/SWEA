for tc in range(1, 1 + int(input())):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    high = 21
    start_lst = []

    for r in range(N):
        for c in range(N):
            if arr[r][c] > high:
                temp_max = arr[r][c]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == high:
                start_lst.append([r, c])

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]


