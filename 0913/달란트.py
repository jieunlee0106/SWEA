for t in range(int(input())):
    n, p = map(int, input().split())
    if n%p == 0:
        result = (n/p)**p
    else:
        r = n%p
        result = ((n//p)**(p-r))*(n//p+1)**r
    print(f'#{t+1}', int(result))