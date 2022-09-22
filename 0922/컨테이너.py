for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    container = list(map(int, input().split()))
    truck = sorted(list(map(int, input().split())))
    container.sort(reverse=True)

    ret = 0

    t = len(truck)-1
    for c in container:
        if t >= 0:
            if c <= truck[t]:
                ret += c
                t -= 1
            else:
                continue

        else: break

    print(f'#{tc} {ret}')