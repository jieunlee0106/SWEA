'''
ex = 2 7
v[2] = 0
v[3] = 1,               v[1] = 1,                v[4] = 1
v[6] = 2,               v[0] = 2,                v[5] = 2, v[8] = 2,
v[7] = 3 (return)
'''
from collections import deque

def bfs():
    q = deque([s])
    while q:
        n = q.popleft()
        if n == e:
            return visited[n]
        for i in range(4):
            if i == 0:
                k = n + 1
            elif i == 1:
                k = n - 1
            elif i == 2:
                k = n * 2
            elif i == 3:
                k = n - 10
            if 0 <= k <= maxx and not visited[k]:
                visited[k] = visited[n] + 1
                q.append(k)


for tc in range(1, int(input()) + 1):
    s, e = map(int, input().split())
    maxx = 10 ** 6
    visited = [0] * (maxx + 1)
    print(f'#{tc} {bfs()}')

