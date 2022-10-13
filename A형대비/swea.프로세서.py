def line(r ,c):
    for d in range(4):
        R = r + dr[d]
        C = c + dc[d]
        if 0 <= R < N and 0 <= C < N:
            pass

for tc in range(1, int(input())+ 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    chip_lst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                if i == 0 or j == 0 or i == N - 1 or j == N - 1:
                    arr[i][j] = 2       # 연결 됨
                else:
                    line(i, j)

