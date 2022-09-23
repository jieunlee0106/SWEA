from itertools import product

def dfs(r, c):
    global ret, cnt
    for l in range(len(ans)):
        R = r
        C = c
        for change in range(4):
            R = R + dr[change]*ans[l][change]
            C = C + dc[change]*ans[l][change]

            if 0 <= R < n and 0 <= C < n:
                if shop[R][C] not in cnt_lst:
                    cnt_lst.append(shop[R][C])
                    cnt += shop[R][C]

                else:
                    cnt = 0
                    break
            else:
                cnt = 0
                break
        if cnt != 0:
            retlst.append(cnt)
    return retlst



for tc in range(1, int(input())+1):
    n = int(input())
    shop = [list(map(int, input().split())) for _ in range(n)]

    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]


    cnt_lst = [cc for cc in range(1, n-1)]
    ans = []
    for i in (product(cnt_lst, repeat=2)):
        ans.append(list(i))
    ans.remove([n - 2, n - 2])
    for i in range(len(ans)):
        ans[i].extend([ans[i][0], ans[i][1]])

    ret = -1


    for r in range(n):
        cnt = 0
        for c in range(n):
            retlst = []
            dfs(r, c)

    print(retlst)