for t in range(1, int(input())+1) :
    n = int(input())
    result = round(pow(n, 1/3))

    if result ** 3 == n :
        print(f'#{t}', result)
    else :
        print(f'#{t}', -1)
