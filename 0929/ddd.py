def check(cur_lst1, r, C2, k):
    global ret2, lst
    if k >= 4:
        for kk in lst:
            ret2 += kk**2
        print(ret2)
        ret2 = 0
        return
    for ii in cur_lst1:
        if ii not in lst and ii > lst[-1]:
            lst.append(ii)
            check(cur_lst1, r, C2, k + ii)
            lst.pop()
ret2 = 0
lst = [0]
check([1, 2, 3], 0, 0, 0)
