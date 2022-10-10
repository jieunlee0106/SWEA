from collections import deque
import sys
sys.setrecursionlimit(100000)

def island(num, r, c):
    for d in range(4):
        R = r + dr[d]
        C = c + dc[d]
        if 0 <= R < N and 0 <= C < N:
            if arr[R][C] == 1 and visited[R][C] == 0:
                visited[R][C] = 1
                arr[R][C] = num
                island(num, R, C)


def bfs(n):
    global ret
    q = deque()
    for r in range(N):
        for c in range(N):
            if arr[r][c] == n:
                q.append((r, c))
                check[r][c] = 1

    while q:
        r, c = q.popleft()
        for d in range(4):
            R = r + dr[d]
            C = c + dc[d]
            if 0 <= R < N and 0 <= C < N:
                if arr[R][C] != 0 and arr[R][C] != n:
                    ret = min(ret, check[r][c])
                    return
                if arr[R][C] == 0 and check[R][C] == 0:
                    check[R][C] = check[r][c] + 1
                    q.append((R, C))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

island_num = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            arr[i][j] = island_num
            island(island_num, i, j)
            island_num += 1

island_cnt = island_num

ret = 10000
for n in range(1, island_cnt):
    check = [[0] * N for _ in range(N)]
    bfs(n)
print(arr)
print(ret - 1)