def cal(k, h):
    global ret, lst, d, maxx, mini
    if k == n - 1:
        aaa = ''.join(str(arr))
        if aaa not in d:
            d[aaa] = 1
            for q in range(1, len(arr)-1, 2):
                if arr[q] == '+':
                    ret += arr[q + 1]
                elif arr[q] == '-':
                    ret -= arr[q + 1]
                elif arr[q] == '*':
                    ret *= arr[q + 1]
                elif arr[q] == '/':
                    ret //= arr[q + 1]
            maxx = max(maxx, ret)
            mini = min(mini, ret)
            ret = arr[0]
        return

    for r in range(1, len(arr)-1, 2):
        if used[h] == 0 and arr[r] == 0:
            used[h] = 1
            arr[r] = oper[h]
            cal(k+1, h+1)
            arr[r] = 0
            used[h] = 0


for tc in range(1, int(input())+1):

    n = int(input())
    maxx = -10000000
    mini = 100000000
    oper_temp = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    lst = []
    oper = [0]*(n-1)
    arr = [0]*(2*n-1)
    idx = 0
    opp = ['+', '-', '*', '/']
    for i in range(4):
        for j in range(idx, idx + oper_temp[i]):
            oper[j] = opp[i]
        idx = idx + oper_temp[i]

    used = [0]*(n-1)
    d = {}
    idx = 0
    for o in range(0, len(arr), 2):
        arr[o] = nums[idx]
        idx += 1
    ret = arr[0]
    cal(0, 0)

    print(f'#{tc} {maxx - mini}')
