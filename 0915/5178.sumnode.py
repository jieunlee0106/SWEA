for t in range(int(input())):
    n, m, l = map(int, input().split())
    h = [0] * (n+1)
    for _ in range(m):
        node, num = map(int, input().split())
        h[node] = num
    if n%2 != 0:
        for i in range(n, 0, -1):
            if h[i] == 0:
                h[i] = h[i*2] + h[i*2+1]
    else:
        for i in range(n, 0, -1):
            if i != n/2:
                if h[i] == 0:
                    h[i] = h[i*2] + h[i*2+1]
            else:
                if h[i] == 0:
                    h[i] = h[i*2]
    print(f'#{t+1}', h[l])
