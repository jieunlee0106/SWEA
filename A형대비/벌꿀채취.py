def check(cur_lst1, r, C,  k):
    global ret2, k_lst, ret_lst, visited
    if k > S:
        return
    if min(cur_lst1) <= k <= S:
        for kk in k_lst:
            ret2 += kk**2
        if [ret2, r, C] not in ret_lst:
            ret_lst += [[ret2, r, C]]
        ret2 = 0
        return
    for ii in range(M):
        if ii not in visited and ii > visited[-1]:
            k_lst.append(cur_lst1[ii])
            visited.append(ii)
            check(cur_lst1, r, C,  k + cur_lst1[ii])
            k_lst.pop()
            visited.pop()

def Honey(C):
    global ret_lst, visited
    for r in range(N):
        ret = 0
        honey = []
        for c in C:
            if arr[r][c] != 0:
                honey.append(arr[r][c])
        if sum(honey) <= S:
            for h in honey:
                ret += h**2
            ret_lst += [ret]


        else:
            bits = []
            check(honey, r, C, 0)

for tc in range(1, int(input())+1):
    N, M, S = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = []
    for i in range(0, N - M + 1):
        temp = []
        for j in range(i, i + M):
            temp.append(j)
        lst.append(temp)

    ret2 = 0
    k_lst = []
    ret_lst = []
    visited = [-1]
    for c_lst in lst:
        Honey(c_lst)

    maxx = 0
    rr = 0
    cc = []
    for res, r, ccc in ret_lst:
        if res > maxx:
            maxx = res
            rr = r
            cc = ccc
    ret_lst.remove([maxx, rr, cc])

    maxx2 = 0
    rr2 = 0
    cc2 = []
    for res2, r2, ccc2 in ret_lst:
        if res2 > maxx and r2 != rr:
            maxx2 = res2
            rr2 = r2
            cc2 = ccc2


    print(f'#{tc}', maxx + maxx2)