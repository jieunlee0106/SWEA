for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    # 그래프 표시할 2차원 행렬
    # visited(방문처리, 거리계산)
    visited = [0] * (V + 1)
    G = [[] for _ in range(V + 1)]
    Q = []
    # 양방향 설정
    for i in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    start, end = map(int, input().split())

    def bfs(start, end):
        # 시작점 설정 및 방문처리
        Q.append(start)
        visited[start] = 0
        while Q:
            v = Q.pop(0)
            for w in G[v]:
                # 방문하지 않았다면
                if not visited[w]:
                    # 방문처리하고 거리 설정
                    visited[w] = visited[v] + 1
                    Q.append(w)
                    # 도착하면 거리 반환
                    if w == end:
                        return visited[w]
        return 0

    print(f'#{tc}', int(bfs(start, end)))