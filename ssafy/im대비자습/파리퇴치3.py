dr = [-1, 1, 0, 0]
xdr = [-1, 1, -1, 1]
dc = [0, 0, 1, -1]
xdc = [-1, 1, 1, -1]

def fly():
    max_cnt = 0
    for r in range(n):
        for c in range(n):
            ncnt = arr[r][c]
            xcnt = arr[r][c]
            for i in range(4):
                for j in range(1, m):
                    nr = r + dr[i]*j
                    nc = c + dc[i]*j
                    if 0 <= nr < n and 0 <= nc < n:
                        ncnt += arr[nr][nc]

            for i in range(4):
                for j in range(1, m):
                    xnr = r + xdr[i]*j
                    xnc = c + xdc[i]*j
                    if 0 <= xnr < n and 0 <= xnc < n:
                        xcnt += arr[xnr][xnc]

            if xcnt > max_cnt:
                max_cnt = xcnt
            if ncnt > max_cnt:
                max_cnt = ncnt

    return max_cnt

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{t}', fly())