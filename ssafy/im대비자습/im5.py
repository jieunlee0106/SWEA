for t in range(1, int(input())+1):
    n = int(input())
    lst = list(input().split())
    lst1 = lst[:(n+1)//2]
    lst2 = lst[(n+1)//2:]
    new = []
    k = 0
    p = 0
    for i in range(n):
        if i%2 == 0:
            new.append(lst1[k])
            k += 1
        else:
            new.append(lst2[p])
            p += 1
    print(f'#{t}', *new)