
T = int(input())
for t in range(T):
    n = int(input())
    bus_stop = []
    max_count = 0
    for i in range(n):
        bus, a, b = map(int, input().split())
        if bus == 1:
            for s in range(a, b+1):
                bus_stop.append(s)
        elif bus == 2:
            bus_stop.append(a)
            bus_stop.append(b)
            for s in range(a, b):
                if a % 2 == 0 and s % 2 == 0 and s != a and s != b:
                    bus_stop.append(s)
                elif a % 2 == 1 and s % 2 == 1  and s != a and s != b:
                    bus_stop.append(s)
        else:
            bus_stop.append(a)
            bus_stop.append(b)
            for s in range(a, b):
                if a % 2 == 0 and s % 4 == 0 and s != a and s != b:
                    bus_stop.append(s)
                if a % 2 == 1 and s % 3 == 0 and s % 10 != 0 and s != a and s != b:
                    bus_stop.append(s)
    bus_stop.sort()
    for n in bus_stop:
        if bus_stop.count(n) >= max_count:
            max_count = bus_stop.count(n)
        elif bus_stop.count(n) < max_count:
            bus_stop.remove(n)
    print(f'#{t + 1}', max_count)

