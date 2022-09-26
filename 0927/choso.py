import itertools

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    lst = [i for i in range(n)]
    p = list(itertools.permutations(lst, n))
    res = 100000
    ret = 0
    back = 0
    for i in range(len(p)):
        idx = 0
        ret = 0
        back = 0
        for j in range(n):
            ret += arr[idx][p[i][j]]
            idx += 1
            if ret > res:
                back = 1
                break
            if back == 1: break
        res = min(ret, res)
    print(f'#{tc} {res}')