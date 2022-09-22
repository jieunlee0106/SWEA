def go(r, k):
    global c
    global cur_sum

    if k == n-1:
        for k in range(n - 1):
            c = ans[k]
            cur_sum += arr[r][c]
            r = ans[k]
        cur_sum += arr[r][0]
        ret.append(cur_sum)
        r = 0
        cur_sum = 0
        return

    for i in range(n-1):
        if lst[i] not in ans:
            ans.append(lst[i])
            go(r, k+1)
            ans.pop()

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    lst = [i for i in range(1, n)]
    c = 0
    ans = []
    ret = []
    cur_sum = 0
    go(0, 0)
    print(f'#{tc} {min(ret)}')

