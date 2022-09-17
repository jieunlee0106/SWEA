for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [[0]*n for _ in range(3*n-2)]
    lst = []
    for _ in range(n):
        lst += map(int, input().split())
    idx = 0
    for r in range(n-1, 2*n-1):
        for c in range(n-1, 2*n-1):
            arr[r][c] = lst[idx]
            idx += 1

    security = [k for k in range(1, 20, 2)]
    security_k = []
    for k in security:
        if k >= n:
            security_k.append(k)
        else:
            break



