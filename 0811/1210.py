for t in range(10):

    T = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]
    end = 0
    for i in range(100):
        if ladder[99][i] == 2:
            end = i
    c = end
    for r in range(99, 0, -1):
        if c > 0 and ladder[r][c-1] == 1:
            while c > 0 and ladder[r][c-1] == 1:
                c -= 1
        elif c < 99 and ladder[r][c+1] == 1:
            while c < 99 and ladder[r][c+1] ==1:
                c += 1
    print(f'#{t+1}', c)