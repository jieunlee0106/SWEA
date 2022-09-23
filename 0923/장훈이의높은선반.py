
def tower(k):
    global ret, cur_sum

    if k == n:
        for i in range(n):
            if ans[i] == 1:
                cur_sum += members[i]
        if cur_sum >= b:
            ret.append(cur_sum)
        cur_sum = 0
        return

    else:
        ans[k] = 0
        tower(k+1)
        ans[k] = 1
        tower(k+1)


for tc in range(1, int(input())+1):
    n, b = map(int, input().split())
    members  = list(map(int, input().split()))
    cur_sum = 0
    ans = [0]*n
    ret = []
    tower(0)
    print(f'#{tc} {min(ret)-b}')