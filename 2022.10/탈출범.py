def bfs():
    global start_lst, time

    while start_lst:
        r, c = start_lst.pop(0)
        k = visited[r][c]
        go = pipe[arr[r][c]]

        for g in range(len(go)):
            R = r + dr[go[g]]
            C = c + dc[go[g]]
            if 0 <= R < N and 0 <= C < M:
                if arr[R][C] and not visited[R][C]:
                    if f[go[g]] in pipe[arr[R][C]]:
                        visited[R][C] = k+1
                        start_lst += [[R, C]]



    return
for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]

    pipe = {1: [1, 2, 3, 4], 2: [1, 2], 3: [3, 4], 4: [1, 4], 5: [2, 4], 6: [2, 3], 7: [1, 3]}

    f = {1: 2, 2: 1, 3: 4, 4: 3}
    visited = [[0]*M for _ in range(N)]

    start_lst = [[R, C]]
    visited[R][C] = 1
    time = 0
    bfs()

    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1
    print(f'#{tc} {cnt}')
