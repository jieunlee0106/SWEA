
def Honey(pot_lst):
    global honey
    if sum(pot_lst) <= S:
        for h in pot_lst:
            honey += h**2
        return honey
    else:
        possible(pot_lst, 0)
        return honey

def possible(pot_lst, k):
    global honey, possible_pot, maxx, honey_lst
    if sum(possible_pot) > S:
        return

    if sum(possible_pot) <= S:
        honey = 0
        for h in possible_pot:
            honey += h**2
        honey_lst += [honey]

    if k >= M:
        return
    possible_pot.append(pot_lst[k])
    possible(pot_lst, k + 1)
    possible_pot.pop()
    possible(pot_lst, k + 1)


for tc in range(1, int(input()) + 1):
    N, M, S = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    pot = []
    for r in range(N):
        idx = 0
        while idx <= N - M:
            temp_pot = []
            for c in range(idx, idx + M):
                temp_pot += [arr[r][c]]
            honey = 0
            possible_pot = []
            maxx = 10000000
            honey_lst = []
            Honey(temp_pot)
            if honey_lst:
                honey = max(honey_lst)
            pot += [[honey, r, idx, idx + M - 1]]
            idx += 1

    ret_pot = sorted(pot, key=lambda x:x[0], reverse=True)
    ret1 = ret_pot[0][0]
    ret1_r = ret_pot[0][1]
    ret1_s = ret_pot[0][2]
    ret1_e = ret_pot[0][3]
    ret2 = 0
    for ret, r, s, e in ret_pot[1:]:
        if r != ret1_r:
            ret2 = ret
            break
        else:
            if ret1_s <= s <= ret1_e or ret1_s <= e <= ret1_e:
                continue
            else:
                ret2 = ret
                break

    # print(pot)
    # print(ret_pot)
    print(f'#{tc} {ret1+ret2}')