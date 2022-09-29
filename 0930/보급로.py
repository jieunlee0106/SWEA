# dfs 시간 초과 / 4 번 tc 까지 겨우 돌아감
from collections import deque
def bfs(r, c):

    q = deque()
    q. append((r, c))
    s = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            R = r + dr[i]
            C = c + dc[i]
            if 0 <= R < n and 0 <= C < n :
                if time[R][C] > arr[R][C] + time[r][c]:
                    time[R][C] = arr[R][C] + time[r][c]
                    q.append((R, C))
    return
for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    time = [[10000]*n for _ in range(n)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    time[0][0] = 0
    bfs(0, 0)
    print(f'#{tc}', time[n-1][n-1])
