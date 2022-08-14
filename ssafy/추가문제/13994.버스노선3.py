# 방법1에서는 input 값을 bus, a,b 라는 변수로 각각 받고 / 노선번호를 리스트에 담고 그 번호의 개수를 일일히 알아보았다.
#실행시간 초과로 이번 식에서는 input값을 list로 받고 인덱스를 통해 계산을 하였고, 노선 번호를 전체 노선에 바로 넣는 방식으로 계산을 했다.
#방법 1과 방법 2는 실행시간이 5배가 넘게 차이가 났는데, 어느 부분이 이렇게 큰 차이를 만들어 냈는지..?
T = int(input())
for t in range(T):
    n = int(input())
    bus_stop = list(0 for _ in range(1001))
    bus_a_b = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        bus_stop[bus_a_b[i][1]] += 1
        bus_stop[bus_a_b[i][2]] += 1

        if bus_a_b[i][0] == 1:
            for s in range(bus_a_b[i][1]+1, bus_a_b[i][2]):
                bus_stop[s] += 1

        elif bus_a_b[i][0] == 2:

            for s in range(bus_a_b[i][1], bus_a_b[i][2], 2):
                if s != bus_a_b[i][1]:
                    bus_stop[s] += 1

        elif bus_a_b[i][0] == 3:
            for s in range(bus_a_b[i][1], bus_a_b[i][2]):
                if bus_a_b[i][1] % 2 == 0 and s % 4 == 0 and s != bus_a_b[i][1]:
                    bus_stop[s] += 1
                elif bus_a_b[i][1] % 2 == 1 and s % 3 == 0 and s % 10 != 0 and s != bus_a_b[i][1]:
                    bus_stop[s] += 1
    max_stop = 0
    for b_n in bus_stop:
        if b_n > max_stop:
            max_stop = b_n
    print(f'#{t + 1}', max_stop)
