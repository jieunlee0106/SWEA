for t in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split()))
    man = [0]*11115
    result = 0
    bbb = 'Possible'
    bcnt = 0

    for k in range(n):
        man[lst[k]] -= 1

    for j in range(1, 11115):
        if bcnt < 0:
            bbb = 'Impossible'
            break
        if j % m == 0:
            bcnt += bcnt + k + man[j]
        elif j % m != 1:
            bcnt += bcnt + man[j]
    print(f'#{t}', bbb)