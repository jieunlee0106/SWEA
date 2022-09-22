def back(r, c):
    global cur_sum, ret

    if ret <= cur_sum:
        return
    if r == n-1 and c == n-1:
        ret = cur_sum
        return

    for i in range(2):
        R = r + dr[i]
        C = c + dc[i]
        if 0 <= R < n and 0 <= C < n:
            if (R, C) not in visited:
                visited.append((R, C))
                cur_sum += arr[R][C]
                back(R, C)
                cur_sum -= arr[R][C]
                visited.remove((R, C))
        else: continue


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dr = [1, 0]
    dc = [0, 1]
    ret = 100000
    visited = []
    cur_sum = arr[0][0]
    back(0, 0)
    print(f'#{tc} {ret}')