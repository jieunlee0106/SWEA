def re(d, r, i, c):
    if d == 0:
        for j in range(i+1, r):
            arr[j][c] = 0
    if d == 1:
        for j in range(r+1, i):
            arr[j][c] = 0
    if d == 2:
        for j in range(i+1, c):
            arr[r][j] = 0
    if d == 3:
        for j in range(c+1, i):
            arr[r][j] = 0
    return

def back(k, line):
    global ret, core

    if k == K:
        ret = min(line, ret)

        print('#', ret)
        for kk in range(N):
            print(arr[kk])
        print()
        return

    r, c = core[k]

    for d in range(4):
        # 상
        check = 0
        if d == 0:
            for i in range(r-1, -1, -1):
                if arr[i][c] == 1:
                    re(d, r, i, c)
                    check += 1
                    break
                else:
                    arr[i][c] = 1
            if check == 0:
                back(k + 1, line + r)

        # 하
        check = 0
        if d == 1:
            for i in range(r+1, N):
                if arr[i][c] == 1:
                    re(d, r, i, c)
                    check += 1
                    break
                else:
                    arr[i][c] = 1
            if check == 0:
                back(k + 1, line + N - 1 - r)

        # 좌
        check = 0
        if d == 2:
            for i in range(c-1, -1, -1):
                if arr[r][i] == 1:
                    re(d, r, i, c)
                    check += 1
                    break
                else:
                    arr[i][c] = 1
            if check == 0:
                back(k + 1, line + c)

        # 우
        check = 0
        if d == 3:
            for i in range(c+1, N):
                if arr[r][i] == 1:
                    re(d, r, i, c)
                    check += 1
                    break
                else:
                    arr[r][i] = 1
            if check == 0:
                back(k + 1, line + N - 1 - c)
    return

def line(r, c):
    for d in range(4):
        R = r + dr[d]
        C = c + dc[d]
        if 0 <= R < N and 0 <= C < N:
            pass

for tc in range(1, int(input())+ 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    ret = 1000000
    core = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if arr[i][j] == 1:
                core.append([i, j])
    K = len(core)
    r, c = core[0]
    back(0, 0)
    print(ret)