T = int(input())

for t in range(T):
    n = int(input())
    carrot = list(map(int, input().split()))

    cnt = 1
    b_c = []

    for i in range(1, n+1):
        if carrot[i] > carrot[i-1]:
            cnt += 1
            b_c.append(cnt)
        else:
            cnt = 1
    print(f'#{t+1}', max(b_c))