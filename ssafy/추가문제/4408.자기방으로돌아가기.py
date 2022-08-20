for t in range(1, int(input())+1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    corridor = [0]*201
    for r in range(n):
        if room[r][0] > room[r][1]:
            room[r] = [room[r][1], room[r][0]]
    for i in range(n):
        l = room[i][0]
        r = room[i][1]
        s = 0
        e = 0
        if l % 2 == 0:
            s = l//2-1
            if r % 2 == 0:
                e = r//2 - 1
            elif r % 2 == 1:
                e = r//2
        elif l % 2 == 1:
            s = l//2
            if r % 2 == 0:
                e = r//2 - 1
            elif r % 2 == 1:
                e = r // 2
        for d in range(s, e+1):
                corridor[d] += 1
    print(f'#{t}', max(corridor))
