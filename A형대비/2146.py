
import sys
sys.setrecursionlimit(100000)

def island(num, r, c):
    for d in range(4):
        R = r + dr[d]
        C = c + dc[d]
        if 0 <= R < N and 0 <= C < M:
            if arr[R][C] == 1 and visited[R][C] == 0:
                visited[R][C] = 1
                arr[R][C] = num
                island(num, R, C)

def bridge(lst):
    for i in range(N):
        u, v, w,  = 0, 0, 0
        cnt = 0
        for j in range(M):
            if arr[i][j] != 0:
                if u == 0 and v == 0:
                    u = arr[i][j]
                elif u != 0 and cnt != 0:
                    v = arr[i][j]
                    if v != u:
                        if cnt >= 2:
                            lst += [[u, v, cnt]]
                        u, v, cnt = arr[i][j], 0, 0
                    elif v == u:
                        v, cnt = 0, 0
            else:
                if u != 0 and v == 0:
                    cnt += 1


    for j in range(M):
        u, v, w, = 0, 0, 0
        cnt = 0
        for i in range(N):
            if arr[i][j] != 0:

                if u == 0 and v == 0:
                    u = arr[i][j]
                elif u != 0 and cnt != 0:
                    v = arr[i][j]
                    if v != u:
                        if cnt >= 2:
                            lst += [[u, v, cnt]]
                        u, v, cnt = arr[i][j], 0, 0
                    elif v == u:
                        v, cnt = 0, 0
            else:
                if u != 0 and v == 0:
                    cnt += 1

def prim(r, V):     # 섬의 개수 = V - 1
    MST = [0]*(V)
    MST[r] = 1
    s = 0
    for _ in range(2, V):
        u = 1
        minV = 10000
        for i in range(1, V):
            if MST[i] == 1:
                for j in range(1, V):
                    if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
                        u = j
                        minV = adjM[i][j]

        s += minV
        # print(minV, u, s)
        MST[u] = 1
        # print(MST)
    for m in MST[1:]:
        if m == 0:
            return -1
    return s


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

island_num = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            arr[i][j] = island_num
            island(island_num, i, j)
            island_num += 1
lst = []
bridge(lst)
if len(lst) == 0:
    print(-1)

else:
    bridge = []
    for lst1 in lst:
        if lst1 not in bridge:
            bridge.append(lst1)
    adjM = [[0] * (island_num + 1) for _ in range(island_num + 1)]
    print(bridge)
    print(adjM)
    for u, v, w in bridge:
        if adjM[u][v] and adjM[u][v] < w:
            continue
        adjM[u][v] = w
        adjM[v][u] = w
    print(adjM)
    # print(bridge)
    # print(adjM)
    print(prim(1, island_num))


#
# 4 8
# 0 0 0 0 0 0 1 1
# 1 0 0 1 1 0 1 1
# 1 1 1 1 0 0 0 0
# 1 1 0 0 0 1 1 0

# 2 5
# 1 0 0 0 0
# 0 0 0 1 0

# 5 6
# 1 1 0 0 0 1
# 1 1 0 0 0 1
# 0 0 0 0 0 1
# 0 0 0 0 0 1
# 1 1 1 1 1 1

# 6 6
# 1 1 1 1 1 1
# 0 0 0 0 0 0
# 1 1 1 0 1 0
# 0 1 0 1 0 1
# 0 0 0 0 0 0
# 1 1 1 1 1 1

# 8 8
# 0 0 0 1 1 1 1 0
# 0 1 1 1 1 0 1 0
# 0 1 0 1 1 1 0 0
# 0 1 0 0 0 1 0 0
# 0 0 0 1 0 0 1 0
# 0 0 0 0 0 1 0 0
# 0 1 1 1 0 0 0 0
# 0 1 0 0 0 1 0 0

# 8 6
# 0 1 0 0 1 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 1 0 0 1 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 1 1 1 1 0
