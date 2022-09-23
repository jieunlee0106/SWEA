for tc in range(1, int(input())+1):
    tw = list(map(int, input()))
    th = list(map(int, input()))
    tw_l = len(tw)
    th_l = len(th)
    ret2_lst = []
    ret3_lst = []
    ret = 0
    d = {}

    for i in range(tw_l):
        if tw[i] == 0:
            tw[i] = 1

            s = tw_l - 1
            ret2 = 0

            for j in range(tw_l):
                if tw[j] == 1:
                    ret2 += 2**s
                    s -= 1
                else:
                    s -= 1
            ret2_lst.append(ret2)
            tw[i] = 0

        else:
            tw[i] = 0

            s = tw_l - 1
            ret2 = 0

            for j in range(tw_l):
                if tw[j] == 1:
                    ret2 += 2 ** s
                    s -= 1
                else:
                    s -= 1
            ret2_lst.append(ret2)
            tw[i] = 1

    for o in range(th_l):
        if ret != 0: break
        else:
            if th[o] == 2:
                th[o] = 1
                temp_th = ''.join(str(i) for i in th)
                if int(temp_th, 3) in ret2_lst:
                    ret = int(temp_th, 3)
                    break

                th[o] = 2

                th[o] = 0
                temp_th = ''.join(str(i) for i in th)
                if int(temp_th, 3) in ret2_lst:
                    ret = int(temp_th, 3)
                th[o] = 2

            elif th[o] == 1:
                th[o] = 2
                temp_th = ''.join(str(i) for i in th)
                if int(temp_th, 3) in ret2_lst:
                    ret = int(temp_th, 3)
                    break

                th[o] = 1

                th[o] = 0
                temp_th = ''.join(str(i) for i in th)
                if int(temp_th, 3) in ret2_lst:
                    ret = int(temp_th, 3)
                th[o] = 1

            else:
                th[o] = 1
                temp_th = ''.join(str(i) for i in th)
                if int(temp_th, 3) in ret2_lst:
                    ret = int(temp_th, 3)
                    break

                th[o] = 0

                th[o] = 2
                temp_th = ''.join(str(i) for i in th)
                if int(temp_th, 3) in ret2_lst:
                    ret = int(temp_th, 3)
                th[o] = 0

    print(f'#{tc} {ret}')