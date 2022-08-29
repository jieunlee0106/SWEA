# 달팽이
for t in range(1, int(input())+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    num = 1
    j = 0
    arr[0][0] = num
    for r in range(n):
        for c in range(n):
            num += 1
            nr = r + dr[j]
            nc = c + dr[j]
            if arr[nr][nc] != 0 or nr < 0 or nc < 0 or nr >= n or nc >= n:
                nr = -r -dr[j-1]
                nc = -c -dc[j-1]
                j += (j + 1) % 4
                nr = r + dr[j]
                nc = c + dr[j]
                arr[nr][nc] = num
            else:
                arr[nr][nc] = num
    print(f'#{t}', arr)