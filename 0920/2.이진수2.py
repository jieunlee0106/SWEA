from itertools import combinations

for tc in range(1, int(input())+1):
    n = float(input())
    lst = [0]*13
    for i in range(1, 13):
        lst[i] = (1/2)**i

    ret = []
    for i in range(1, 13):
        if ret:
            break
        else:
            k = list(combinations(lst, i))
            for c in range(len(k)):
                if sum(k[c]) == n:
                    ret = k[c]

    rr = ''
    if ret :
        result = [0]*13
        rrr = ''
        idx = []
        for j in ret:
            if j in lst:
                idx.append(lst.index(j))
        for p in idx:
            result[p] = 1

        result = result[1: idx[-1]+1]
        for r in result:
            rr += str(r)

        print(f'#{tc}', rr)

    else:
        print(f'#{tc}', 'overflow')