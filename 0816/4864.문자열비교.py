T = int(input())
for t in range(T):
    p = input()
    t = input()
    m = len(p)
    n = len(t)
    result = 0
    i = 0
    j = 0
    while j < m and i < n:
        if p[i] == t[j]:
            i, j = i + 1, j + 1
        else:
            j = j - i + 1
            i = 0
    if j == m:
        result = 1
    else:
        result = 0

    print(f'#{t+1}', 'result')

# T = int(input())
# for t in range(T):
#     s_str = [input() for _ in range(2)]
#     if s_str[0] in s_str[1]:
#         result = 1
#     else:
#         result = 0
#     print(f'#{t+1}', result)