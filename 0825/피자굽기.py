for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))
    out = 0
    for p in range(m):
        pizza[p] = [pizza[p], p]
    pit = [0]*n
    pizza_i = n
    result = 0
    out_list = []

    for i in range(n):
        pit[i] = pizza[i]

    while result == 0:
        if out == n - 1:
            for p in range(n):
                if pit[p][0] != 0:
                    result = pit[p][1] + 1
                    break
        for c in range(n):#cook > //2
            #피자 굽기

            if out != n-1:
                pit[c][0] = pit[c][0]//2
                if pit[c][0] ==0:    #구워진 피자나오면 화덕에서 내보내고 새피자 갖고오기
                    if pizza_i+1 <= m:
                        pit[c] = pizza[pizza_i]
                        pizza_i += 1
                    elif pit[c] not in out_list:
                        out += 1
                        out_list.append(pit[c])
            elif out == n-1:
                for p in range(n):
                    if pit[p][0] != 0:
                        result = pit[p][1] + 1
                        break

    print(f'#{t}', result)
