def PRIM(r, V):
    mst = [0]*(V+1)     # MST 포함여부
    mst[r] = 1
    s = 0               # 이동한 간선들의 가중치 합
    for _ in range(V):
        u = 0           # 가중치가 최소인 정점
        minS = 10**6        # 11 가능
        for i in range(V+1):    # MST에 포함된 정점i와 인접한 정점j 중 MST에 포함되지 않고 가중치가 최소인 정점 u찾기
            if mst[i] == 1:
                for j in range(V+1):
                    if minS > M[i][j] > 0 and mst[j] == 0:
                        u = j
                        minS = M[i][j]
        s += minS
        mst[u] = 1
    return s

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    M = [[0]*(V+1) for _ in range(V+1)]         # 인접한 정점들의 가중치를 나타내는 배열
    for _ in range(E):
        u, v, w = map(int, input().split())
        M[u][v] = w
        M[v][u] = w

    print(f'#{tc}', PRIM(0, V))
