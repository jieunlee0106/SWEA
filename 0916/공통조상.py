for t in range(1, int(input())+1):
    v, e, n1, n2 = map(int, input().split())
    lst = list(map(int, input().split()))
    N = [0] * (v + 1)
    L = [0] * (v + 1)
    R = [0] * (v + 1)

    for i in range(0, e*2, 2):
        if N[lst[i]] == 0:
            N[lst[i]] = 1
            L[lst[i]] = lst[i+1]
        else:
            R[lst[i]] = lst[i+1]

    n1p_lst = []
    n2p_lst = []

    p = n1
    while p != 0:
        p = (p+2)//2
        n1p_lst.append(p)
        if p == 2 or p == 3: break

    p = n2
    while p != 0:
        p = (p+2)//2
        n2p_lst.append(p)
        if p == 2 or p == 3: break

    anc = 0
    for i in n1p_lst:
        for j in n2p_lst:
            if i == j:
                anc = j
                break
            break
    if anc == 0:
        anc = 1
    print(anc)

