T = int(input())
for t in range(T):
    n_q = list(map(int, input().split()))
    box_n = list(0 for _ in range(n_q[0]+1))
    result = []
    for i in range(1, n_q[1]+1):
        L, R = map(int, input().split())
        for n in range(L, R+1):
            box_n[n] = i
    for bn in range(1, n_q[0]+1):
        result.append(box_n[bn])
    print(f'#{t+1}', *result)