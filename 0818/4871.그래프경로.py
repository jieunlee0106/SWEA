T = int(input())
for t in range(T):
    v, e = map(int, input().split())
    num = [list(map(int, input())) for _ in range(e)]
    s, g = map(int, input().split())
    arr = [[0] * v for _ in range(v)]
    lst = []
    for r in range(1, v+1):
        for c in range(1, v+1):
            if [r, c] in num:
                arr[r][c] = 1
            else:
                arr[r][c] = 0

    for i in range(len(num)):
        if num[i][0] == s:
            lst.append(num[i])
    for j in range(len(lst)):
        lst[j][1]


