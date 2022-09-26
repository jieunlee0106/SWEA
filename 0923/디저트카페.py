def go(r, c, change, visited):

    global ret
    eat = len(visited)
    if change == 3:
        if i == r and j == c and eat > 2:
            ret = max(ret, eat)

    if  0 <= r < n and 0 <= c < n and shop[r][c] not in visited:

        p_visited = visited + [shop[r][c]]
        R = r + dr[change]
        C = c + dc[change]
        go(R, C, change, p_visited)

        if change < 3:
            R = r + dr[change+1]
            C = c + dc[change+1]
            go(R, C, change+1, p_visited)

for tc in range(1, int(input())+1):
    n = int(input())
    shop = [list(map(int, input().split())) for _ in range(n)]
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]
    ret = -1
    visited = []
    for i in range(n-1):
        for j in range(1, n-1):
            go(i, j, 0, visited)
    print(f'#{tc} {ret}')
