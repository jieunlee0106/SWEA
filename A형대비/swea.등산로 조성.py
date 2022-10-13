import copy
def back(r, c, k, p, cnt):
    global maxx
    if cnt > maxx:
        maxx = cnt
    arr[r][c] = p
    for d in range(4):
        R = r + dr[d]
        C = c + dc[d]
        if 0 <= R < N and 0 <= C < N:
            if arr[R][C] < p and visited[R][C] == 0:
                visited[R][C] = 1
                back(R, C, k, arr[R][C], cnt + 1)
                visited[R][C] = 0
            else:
                if arr[R][C] - p < K and k == 1 and visited[R][C] == 0:
                    visited[R][C] = 1
                    back(R, C, 0, arr[r][c] - 1, cnt + 1)
                    arr[R][C] = lst[R][C]
                    visited[R][C] = 0

for tc in range(1, 1 + int(input())):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    high = 0
    start_lst = []

    lst = copy.deepcopy(arr)
    for r in range(N):
        for c in range(N):
            if arr[r][c] > high:
                high = arr[r][c]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == high:
                start_lst.append([r, c])

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    maxx = -1

    while start_lst:
        visited = [[0] * N for _ in range(N)]
        r, c = start_lst.pop()
        visited[r][c] = 1
        back(r, c, 1, arr[r][c], 1)
        visited[r][c] = 0

    print(f'#{tc} {maxx}')
