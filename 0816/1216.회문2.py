T = 10
for t in range(T):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    word_lst = []
    max_len = 1
    for r in range(100):
        s = 0
        e = 99
        for c in range(100):
            while s <= e:
                word_lst.clear()
                if arr[r][s] == arr[r][e] and s < e and arr[r][s+1] == arr[r][e-1]:
                    for j in range(s, e+1):
                        word_lst.append(arr[r][j])
                    if word_lst == word_lst[::-1]:
                        if len(word_lst) > max_len:
                            max_len = len(word_lst)
                            break
                    else:
                        if s < e and arr[r][s+1] == arr[r][e]:
                            s += 1
                        elif e > s and arr[r][s] == arr[r][e-1]:
                            e -= 1

                elif s < e and arr[r][s+1] == arr[r][e]:
                    s += 1
                elif e > s and arr[r][s] == arr[r][e-1]:
                    e -= 1


    print(f'#{tc}', max_len)
