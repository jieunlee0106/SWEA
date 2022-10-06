
# 방문정보 표시 - 최적화 문제
# 함수 - Dijkstra(시작정점s, 인접행렬A {arr로 표시} , 거리D)
# V: 모든 정점집합 {이 문제에서는 N}, U: 최단 경로 구성에 선택된 정점집합


# Dijkstra 함수 구현
def dijkstra(s, N):
    U = [0] * (N+1)
    U[s] = 1  # 시작점
    for i in range(N+1):  # 중간의 어떤 지점 i
        D[i] = arr[s][i]  # 시작점에서 중간지점까지의 거리
    for _ in range(N):
        minN = INF
        w = 0  # 가중치 0
        for j in range(N+1):
            if U[j] == 0 and minN > D[j]:  # 미방문 지역이면서, 현재 최소값보다 더 최단거리일 경우
                minN = D[j]  # 최단거리 갱신
                w = j
        U[w] = 1  # 방문 표시
        for k in range(N+1):
            if 0 < arr[w][k] < INF:
                D[k] = min(D[k], D[w] + arr[w][k])  # 둘 중 작은 값


INF = 100000


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())  # N: 마지막 지점 번호  ( 이동: 0 -> N) # E: 간선의 개수
    # 간선들의 리스트 [ [s, e, w], [ , , ], ... ]  # s: 구간 시작 # e: 구간 끝 # w: 구간 거리
    # print(arr)
    # [[0, 1, 1], [0, 2, 6], [1, 2, 1]]
    arr = [[INF]*(N+1) for _ in range(N+1)]
    for l in range(N+1):
        arr[l][l] = 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        arr[s][e] = w
    D = [0] * (N+1)
    dijkstra(0, N)
    # print(D)
    # [0, 1, 2]     # 부분 구간의 최단 경로들의 리스트 # N = 2
    # [0, 9, 3, 7, 4]       # N = 4
    # [0, 10, 7, 17, 10]        # N = 4

    print(f'#{tc} {D[-1]}')
    # 1 2
    # 2 4
    # 3 10