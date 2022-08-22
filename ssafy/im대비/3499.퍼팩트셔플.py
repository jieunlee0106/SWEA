for t in range(1, int(input())+1):
    n = int(input())
    card = input().split()
    for i in range(n):
        front_list = []
        back_list = []
        result = []
        for h in range((n+1)//2):
            front_list.append(card[h])
        for j in range((n+1)//2, n):
            back_list.append(card[j])
        f = 0
        b = 0
        for k in range(1, n+1):
            if k % 2 == 1:
                result.append(front_list[f])
                f += 1
            else:
                result.append(back_list[b])
                b += 1
    print(f'#{t}', *result)