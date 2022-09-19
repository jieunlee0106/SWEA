for t in range(1, int(input())+1):
    h, w = map(int, input().split())
    temp_arr = [list(map(int, input())) for _ in range(h)]
    arr = []
    for r in range(h):
        if 1 in temp_arr[r]:
            arr = temp_arr[r]
            break
        else:
            continue
    num = []
    ret = []
    e = 0

    for c in range(-1, -w, -1):
        if arr[c] == 1:
            e = c
            e = w + e
            break
        else:
            continue

    for cc in range(e-55, e+1):
        num.append(arr[cc])

    cnt_lst = []

    for j in range(0, 56, 7):
        cnt = 1
        now = num[j]
        for ccc in range(j+1, j+7):
            if num[ccc] != now and ccc != j+6:
                now = num[ccc]
                cnt_lst.append(cnt)
                cnt = 1
            elif num[ccc] == now and ccc != j+6:
                cnt += 1
            elif num[ccc] != now and ccc == j+6:
                cnt_lst.append(cnt)
                cnt_lst.append(1)

            elif num[ccc] == now and ccc == j + 6:
                cnt += 1
                cnt_lst.append(cnt)
    f_lst = []
    for k in range(0, 32, 4):
        f_lst = []
        for p in range(k, k+4):
            f_lst.append(cnt_lst[p])
            if f_lst == [3, 2, 1, 1]:
                ret.append(0)
            if f_lst == [2, 2, 2, 1]:
                ret.append(1)
            if f_lst == [2, 1, 2, 2]:
                ret.append(2)
            if f_lst == [1, 4, 1, 1]:
                ret.append(3)
            if f_lst == [1, 1, 3, 2]:
                ret.append(4)
            if f_lst == [1, 2, 3, 1]:
                ret.append(5)
            if f_lst == [1, 1, 1, 4]:
                ret.append(6)
            if f_lst == [1, 3, 1, 2]:
                ret.append(7)
            if f_lst == [1, 2, 1, 3]:
                ret.append(8)
            if f_lst == [3, 1, 1, 2]:
                ret.append(9)
    oo = 0
    ee = 0
    for o in range(0, 8, 2):
        oo += ret[o]
    for e in range(1, 8, 2):
        ee += ret[e]

    rrr = oo*3 + ee

    answer = 0
    if rrr % 10 == 0:
        answer = sum(ret)
    else:
        answer = 0
    print(f'#{t}', answer)