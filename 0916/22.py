def dfs(r, c, cnt):
    global maxcnt
    global visited
    for i in range(4):
        rr = r + d[i][0]
        cc = c + d[i][1]
        if 0 <= rr < n and 0 <= cc < n and [rr, cc] not in visited:
            if arr[rr][cc] == arr[r][c] + 1:

                r = rr
                c = cc
                visited.append([r, c])
                cnt = dfs(r, c, cnt + 1)

    return cnt


for t in range(1, int(input()) + 1):
    n = int(input())
    lst = []
    arr = [list(map(int, input().split())) for _ in range(n)]

    maxcnt = 0
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for r in range(n):
        for c in range(n):
            visited = []
            visited.append([r, c])
            lst.append(dfs(r, c, 1))

    idx = 0
    ret_max = 0
    ret_lst = [[0] * n for _ in range(n)]
    ret_num = []
    for p in range(n):
        for q in range(n):
            ret_lst[p][q] = lst[idx]
            if lst[idx] >= ret_max:
                ret_max = lst[idx]
                idx += 1
            else:
                idx += 1
    for g in range(n):
        for gg in range(n):
            if ret_lst[g][gg] == ret_max:
                ret_num.append(arr[g][gg])

    print(f'#{t}', min(ret_num), ret_max)