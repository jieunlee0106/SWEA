T = int(input())
for t in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    s = 1
    min_f = 0
    a, b = [], []
    food_s = []
    for r in range(n-1):
        for c in range(s, n):
            if r != c:
                food_s.extend([[arr[r][c] + arr[c][r], r, c]])
                s += 1
                continue

    food_s.sort()
    for f in range(1, len(food_s)):
        if food_s[f][0] - food_s[f-1][0] < min_f and (food_s[f][1] != food_s[f-1][1] or food_s[f-1][2]) and (food_s[f][2] != food_s[f-1][1] or food_s[f-1][2]):
            min_f = food_s[f][0] - food_s[f-1][0]
    print(min_f)
