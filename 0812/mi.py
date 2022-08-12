T = int(input())

for t in range(T):
    s = list(input())
    re_s = []
    n = len(s)
    for i in range(len(s)):
        re_s.append(s[-i-1])

    for i in range(len(re_s)):
        if re_s[i] == 'd':
            re_s[i] = 'b'

        elif re_s[i] == 'b':
            re_s[i] = 'd'

        elif re_s[i] == 'p':
            re_s[i] = 'q'

        elif re_s[i] == 'q':
            re_s[i] = 'p'

    print(f'#{t+1}',  ''.join(re_s))