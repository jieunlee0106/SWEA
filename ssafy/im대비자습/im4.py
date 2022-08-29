for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    lst = [0]*(n)

    for k in range(1, m+1):
        s, e = map(int, input().split())
        for j in range(s-1, e):
            lst[j] = k
    print(f'#{t}', *lst)