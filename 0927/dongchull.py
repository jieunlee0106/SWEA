def back(k, idx, res):
    global ret

    if res <= ret:
        return

    if k == n:
        if ret <= res:
            ret = res
            return ret

    for i in range(n):
        if used[i] == 0 and arr[idx][i] != 0:
            used[i] = 1
            back(k+1, idx+1, res * arr[idx][i] / 100)
            used[i] = 0

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ret = -1
    # res = 1
    used = [0]*n
    back(0, 0, 1)
    print(f'#{tc}', '%.6f'%(ret*100))