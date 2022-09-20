import sys; sys.stdin = open('2117.txt')
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    P = []
    line_set = set()

    for _ in range(n):
        t = input().rstrip('0')
        if t:
            line_set.add(t)
            #  2 진수로 변환

    code_set = set()
    for line in line_set:
        i = len(line) -1
        # line을 2 진수 문자열로 변환
        while i >= 0:
            if line[i] == '1':
                codes = []
                # 8번 반복해서 0101 패턴을 반복
                for _ in range(8):
                    # 1 의 개수 카운팅
                    # 0 의 개수 카운팅
                    # 1 의 개수 카운팅
                    # 0 의 개수 카운팅
                    c1 = c2 = c3 = c4 = 0
                    while line[i] == '0': i -= 1
                    while line[i] == '1': c3 += 1; i -= 1
                    while line[i] == '0': c2 += 1; i -= 1
                    while line[i] == '1': c1 += 1; i -= 1
                    ratio = min(c2, c3, c4)
                    codes.append(P[(c2//ratio, c3//ratio, c4//ratio)])
                code_set.add(tuple(codes))

            i -= 1

    ans = 0
    for codes in code_set:
        odd = codes[1] + codes[3] + codes[5] + codes[7]
        even = codes[0] + codes[2] + codes[4] + codes[6]
        if (odd*3 + even) % 10 == 0:
            ans += odd + even
    print(ans)
    break