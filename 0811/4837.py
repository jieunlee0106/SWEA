T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    a = list(range(1, 13))

    n = len(a)

    for i in range(1<<n):
        for j in range(n):
            if i & (1<<j):
