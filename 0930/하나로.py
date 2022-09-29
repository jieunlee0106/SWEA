def prim(r, n):
    pass
    mst = [0]*n
    key =[10000000000]*n
    key[r] = 0

    for _ in range(n):
        u = 0
        minv = 10000000000
        for i in range(n):
            if mst[i] == 0 and key[i] < minv:
                u = i
                minv = key[i]
        mst[u] = 1
        for v in range(n):
            if mst[v] == 0 and G[u][v] > 0 :
                key[v] = min(key[v], G[u][v])
    return sum(key)
for tc in range(1, int(input())+1):
    n = int(input())
    island = [[] for _ in range(n)]
    cordi_x = list(map(int, input().split()))
    cordi_y = list(map(int, input().split()))
    tex = float(input())
    G = [[0]*n for _ in range(n)]
    for i in range(n):
        island[i] = (cordi_x[i], cordi_y[i])
    for r in range(n):
        for c in range(n):
            if r!= c:
                G[r][c] = (abs(island[r][0] - island[c][0])**2 + abs(island[r][1] - island[c][1])**2) * tex
                G[c][r] = (abs(island[r][0] - island[c][0])**2 + abs(island[r][1] - island[c][1])**2) * tex

    print(f'#{tc}', round(prim(0, n)))