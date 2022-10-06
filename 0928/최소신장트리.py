# for tc in range(1, int(input())+1):
#     N, E = map(int, input().split())
#     G = [[] for _ in range(N+1)]
#     for _ in range(E):
#         u, v, weight = map(int, input().split())
#         G[u].append( (v, weight) )
#     D = [0xffffff] * (N + 1)    # 초기값 주ㅡ이
#     D[0] = 0                    # 출발점은 항상 0으로 설정
#    Q = [0]
#
#     while Q:
#         u = Q.pop(0)        # 정점 번호
#         for v, weight in G[u]:
#             # (u, v)간선 완화
#             if D[v] > D[u] + weight:
#                 D[v] = D[u] + weight
#                 Q.append(v)
#     print(f'#{tc} {D[N]}')


def dfs(u):
    for v, weight in G[u]:
        # (u, v)간선 완화
        if D[v] > D[u] + weight:
            D[v] = D[u] + weight
            dfs(v)


for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, weight = map(int, input().split())
        G[u].append( (v, weight) )
    D = [0xffffff] * (N + 1)    # 초기값 주ㅡ이
    D[0] = 0      # 출발점은 항상 0으로 설정
    dfs(0)
    print(f'#{tc} {D[N]}')