for t in range(int(input())):
    size = 1000001
    h = [0] * size
    last = 0
    def push(item):
        global last
        last += 1
        h[last] = item
        c, p = last, last//2
        while p > 0 and h[c] < h[p]:
            h[c], h[p] = h[p], h[c]
            c = p
            p = p // 2


    n = int(input())
    data = list(map(int, input().split()))
    for val in data:
        push(val)
    cnt = 0
    while last//2 > 0:
        last = last//2
        cnt += h[last]
    print(f'#{t+1}', cnt)