T = int(input())
for t in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    s = 0
    for r in range(n-1):
        for c in range(s, n):
            food_s = []
            if r != c:
                food_s.append(arr[r][c] + arr[c][r])
                s += 1
                