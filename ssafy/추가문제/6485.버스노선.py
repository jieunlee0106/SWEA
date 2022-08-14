T = int(input())
for t in range(T):
    all_stop = list(0 for _ in range(5001))
    s_n = []
    N = int(input())
    bus_stop = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    c_stop = list(int(input()) for _ in range(P))
    for i in range(N):
        for s in range(bus_stop[i][0], bus_stop[i][1]+1):
            all_stop[s] += 1
    for c in c_stop:
        s_n.append(all_stop[c])
    print(f'#{t+1}', *s_n)