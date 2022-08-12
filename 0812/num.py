T= int(input())

for t in range(T):
    str1 = list(input())
    str2 = list(input())
    dict_s = {}

    for i in str2:
        if i in str1:
            if i in dict_s:
                dict_s[i] += 1
            else:
                dict_s[i] = 1

    m = max(dict_s.values())

    print(f'#{t+1}', m)