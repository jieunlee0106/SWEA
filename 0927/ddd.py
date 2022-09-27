def tsp(prev, visited):
    if visited == (1 << n) - 1:
        return 1

    if dp[visited]:
        return dp[visited]

    for job in range(n):
        if visited & (1 << job): continue
        dp[visited] = max(
            dp[visited], tsp(prev + 1, visited | (1 << job)) * (graph[prev][job] / 100)
        )
    return dp[visited]


for T in range(int(input())):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (1 << n)
    tsp(0, 0)
    print(f'#{T + 1} {dp[0] * 100:.6f}')