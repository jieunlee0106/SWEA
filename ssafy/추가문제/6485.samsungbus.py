for t in range(int(input())):
    n = int(input())
    bus_stop = [0] * 5001
    bus_list = []
    bus = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    C = [int(input()) for _ in range(p)]
    for i in range(n):
        s, e = bus[i][0], bus[i][1]
        for j in range(s, e+1):
            bus_stop[j] += 1
    for c in C:
        bus_list.append(bus_stop[c])
    print(*bus_list)
