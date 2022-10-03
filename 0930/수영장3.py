t = int(input())
for tc in range(t):
    d, m, m3, y = map(int, input().split())
    plan = list(map(int, input().split()))

    year = [0] * 13
    for i in range(1, 13):
        # 1달: 1일권 VS 1달권
        year[i] = min(year[i - 1] + d * plan[i - 1], year[i - 1] + m)

        # 3달: (1일권 VS 1달권) VS 3달권
        if i >= 3:
            year[i] = min(year[i], year[i - 3] + m3)

    # 1년: ((1일권 VS 1달권) VS 3달권) VS 1년권
    year[12] = min(year[12], y)

    print(f'#{tc + 1} {year[12]}')