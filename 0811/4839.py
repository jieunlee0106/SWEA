T = int(input())

for t in range(T):
    book_ifo = list(map(int, input().split()))
    r = book_ifo[0]
    Pa = book_ifo[1]
    Pb = book_ifo[2]
    l = 1
    c = (l+r)//2
    A_cnt = 0
    B_cnt = 0
    while Pa != c:
        c = (l + r) // 2
        if Pa > c:
            l = c
            A_cnt += 1

        elif Pa < c:
            r = c
            A_cnt += 1
    l = 1
    r = book_ifo[0]
    while Pb != c:
        c = (l + r) // 2
        if Pb > c:
            l = c
            B_cnt += 1
        elif Pb < c:
            r = c
            B_cnt += 1
    if A_cnt < B_cnt:
        win = 'A'
    elif A_cnt > B_cnt:
        win = 'B'
    elif A_cnt == B_cnt:
        win = 0
    print(f'#{t+1}',win )