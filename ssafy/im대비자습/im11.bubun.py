for t in range(1, int(input())):
    n, k = map(int, input().split())
    olst = [k for k in range(1,13)]
    lst = []
    lst3 = []
    for i in range(1<<12):
        for j in range(12):
            if i&(1<<j):
                lst.append(olst[j])
        lst3.append(lst)
    les_lst = []
    for p in range(len(lst3)):
        if len(lst3[p]) == n:
            les_lst.append(p)
    cnt = 0
    for g in les_lst:
        if sum(g) == k:
            cnt += 1
    print(f'#{t}', cnt)