def dfs(r, c, k):
    global ans

    if k == 6:
        anss = ''.join(str(i) for i in ans)
        if anss not in visited:
            visited[int(anss)] = 1
        return

    for i in range(4):
        R = r + dr[i]
        C = c + dc[i]

        if 0 <= R < 4 and 0 <= C < 4 : #and (R, C) not in visitedrc:
            # visitedrc.append((R, C))
            ans.append(arr[R][C])
            dfs(R, C, k+1)
            # visitedrc.remove((R, C))
            ans.pop()

        else:
            continue

for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = {}
    # visitedrc = []
    ret_lst = []
    ret = 0
    for r in range(4):
        for c in range(4):
            # visitedrc = []
            ans = []
            ans.append(arr[r][c])
            # visitedrc.append((r, c))

            dfs(r, c, 0,)
    print(f'#{tc} {len(visited)}')