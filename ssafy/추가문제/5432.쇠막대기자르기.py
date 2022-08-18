T = int(input())

for t in range(T):
    stick = list(input())
    s_list = []
    re_list = []
    s = 0
    for j in range(s, len(stick)):
        l_cnt = 0
        r_cnt = 0
        l = stick[s]
        if stick[j] == '(':
            l_cnt += 1
        else:
            r_cnt += 1
            e = stick.index(stick[j])
            if l_cnt == r_cnt:
                r = stick[j]
                if j - s != 1:
                    s_list.extend([l, r])
                    for i in range(s+1, len(stick)):
                        if stick[i] == '(':
                            s = i
                            break
                elif j - s == 1:
                    re_list.extend([s, j])

    print(s)