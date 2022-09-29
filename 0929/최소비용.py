from collections import deque
def bfs():
    q = deque()
    q.append((0, 0))
    while q:
        r, c = q.popleft()
        for i in range(4):
            R = r + dr[i]
            C = c + dc[i]
            if 0 <= R < n and 0 <= C < n:
                if arr[R][C] >= arr[r][c]:
                    if G[R][C] > G[r][c] + 1 + (arr[R][C] - arr[r][c]):
                        G[R][C] = G[r][c] + 1 + (arr[R][C] - arr[r][c])
                        q.append((R, C))

                else:
                    if G[R][C] > G[r][c] + 1:
                        G[R][C] = G[r][c] + 1
                        q.append((R, C))

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    w = arr[0][0]
    G = [[10000000]*n for _ in range(n)]
    G[0][0] = 0
    # 하우상좌
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    bfs()
    print(f'#{tc} {G[n-1][n-1]}')