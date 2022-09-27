def back(k, lst, idx):
    global ret

    #  가지치기
    if k >= ret:
        return

    if idx >= n:
        ret = min(ret, k)
        k = 0
        return

    for i in range(idx+1, idx + lst[idx] + 1):
        back(k + 1, lst, i)

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    n = arr[0]
    arr[0] = 0
    ret = 10000
    back(-1, arr, 1)

    print(f'#{tc} {ret}')
