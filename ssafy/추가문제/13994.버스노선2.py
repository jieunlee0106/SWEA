
T = int(input())
for t in range(T):
    n = int(input())
    bus_stop = [] #모든 버스의 노선이 들어 갈 리스트, 같은 노선 번호가 있어도 값이 중복해서 들어간다.
    max_count = 0 #가장 많은 버스가 들리는 노선의 개수
    for i in range(n):
        bus, a, b = map(int, input().split())
        bus_stop.append(a) # a 노선은 무조건 들린다.
        bus_stop.append(b) # b 노선은 무조건 들린다포함
        for s in range(a + 1, b): # a, b 는 위에서 포함 했으니까 제외
            if bus == 1: # 버스가 1번 이라면
                bus_stop.append(s) # a, b 사이의 모든 노선번호 추가
            elif bus == 2: # 버스가 2번이라면
                if a % 2 == 0 and s % 2 == 0: # a가 짝수 일 때, 짝수인 번호만 추가
                    bus_stop.append(s)
                elif a % 2 == 1 and s % 2 == 1: # a가 홀수 일 때 홀수인 번호만 추가
                    bus_stop.append(s)
            else: # 버스가 3번 이라면
                if a % 2 == 0 and s % 4 == 0:  #a가 짝수 일 때 4의 배수인 번호만 추가
                    bus_stop.append(s)
                elif a % 2 == 1 and s % 3 == 0 and s % 10 != 0: #a가 홀수 일 때 3의 배수이고 10의 배수가 아닌 번호만 추가
                    bus_stop.append(s)
    bus_stop.sort()
    for n in bus_stop: # 모든 노선의 번호가 들어있는 리스트에서 가장 많은 노선 번호의 개수를 세서 count
        if bus_stop.count(n) >= max_count: # 가장 큰 count 값 출력
            max_count = bus_stop.count(n)
        else:
            bus_stop.remove(n)
    print(f'#{t + 1}', max_count)