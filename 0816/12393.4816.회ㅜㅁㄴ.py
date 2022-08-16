T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    h = []
    r_h = []
    result = []
    for r in range(n):
        s = 0
        for c in range(n - m + 1):
            h.clear()
            r_h.clear()
            for j in range(s, s+m):
                h.append(arr[r][j])

            if len(h) == m:
                for u in range(len(h)):
                    r_h.append(h[-1-u])
            if h == r_h:
                result.append(h)
                h = []
                break
            s += 1

    if len(result) == 0:
        for c in range(n):
            s = 0
            for r in range(n - m + 1):
                h.clear()
                r_h.clear()
                for j in range(s, s+m):
                    h.append(arr[j][c])
                if len(h) == m:
                    for u in range(len(h)):
                        r_h.append(h[-1-u])
                if h == r_h:
                    result.append(h)
                    h = []
                    break
                s += 1

    result = ''.join(result[0])
    print(f'#{t+1}', result)



