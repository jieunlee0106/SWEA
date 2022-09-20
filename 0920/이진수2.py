for tc in range(1, int(input())+1):
    n = int(float(input()) * 10**14)
    lst = list([0]*14 for _ in range(2))
    for i in range(1, 14):
        lst[0][i] = (10**(14-i))*(5**i)
    n_lst = list(str(n))
    z_cnt = 0
    for j in range(len(n_lst)-1, -1, -1):
        if n_lst[j] == '0':
            z_cnt += 1
        else:
            break

    for r in range(len(n_lst)-1, -1, -1):
        if n_lst[r] == '0':
            n_lst.pop()
        else:
            break
    new_n = 0

    for new in range(len(n_lst)):
        new_n *= 10
        new_n += int(n_lst[new])

    i_cnt = 14 - z_cnt
    i_lst = [0]*(i_cnt+1)
    i_len = i_cnt
    for p in range(1, i_cnt+1):
        i_lst[p] = (5**p) * 10**(i_len-p)

    ret1, ret2 = 0, 0
    e = 2
    for s in range(0, len(i_lst)):
        if ret1 != 0 or ret2 != 0:
            break
        else:

            for e in range(s+1, len(i_lst)):
                if i_lst[s] + i_lst[e] == new_n and s != e:
                    ret1, ret2 = s, e
                    break

    ret = [0]*(i_cnt+1)
    ret[ret1] = 1
    ret[ret2] = 1
    result = ''
    for rett in ret[1:]:
        result += str(rett)
    if result != '0':
        print(f'#{tc}', result)
    else:
        print(f'#{tc}', 'overflow')
