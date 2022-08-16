T = int(input())

for t in range(T):
    stick = list(input())
    re = []
    for i in range(len(stick)):
        if stick[i] == '(':
            stick[i] = 0
        else:
            stick[i] = 1

        # ()(((()())(())()))(())
        z_cnt = 0
        o_cnt = 0

        if stick[i] == 0:
            z_cnt += 1
            s = stick.index(stick[i])
            if z_cnt != o_cnt:
                s = stick.index((stick[i]))

        else:
            o_cnt += 1
            e = stick.index(stick[i])
            if z_cnt == o_cnt:
                s_i.extend(s, e)