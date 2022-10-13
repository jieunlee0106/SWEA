
from collections import deque
import sys

def league(i, j):
    global ret, visited
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    re_population = []

    cnt = 0
    cur_sum = 0

    while q:
        r, c = q.pop()
        re_population.append([r, c])
        cur_sum += arr[r][c]
        cnt += 1

        for d in range(4):
            R = r + dr[d]
            C = c + dc[d]
            if 0 <= R < N and 0 <= C < N and visited[R][C] == 0:
                if L <= abs(arr[r][c] - arr[R][C]) <= RR:
                    q.append([R, C])
                    visited[R][C] = 1

    population = cur_sum//cnt
    return population, re_population

N, L, RR = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split()) )for _ in range(N)]
visited = [[0]*N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ret = 0
k = 1
while k != 0:
    k = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                population, re_population = league(i, j)

                if len(re_population) > 1:
                    for nr, nc in re_population:
                        arr[nr][nc] = population
                    k += 1

    visited = [[0] * N for _ in range(N)]

    if k != 0:
        ret += 1

print(ret)

