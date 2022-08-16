T = 10
for t in range(T):
    tc = int(input())
    arr = [list(input()) for _ in range(8)]
    word_lst = []
    max_len = 1
    for r in range(8):
        word_lst = []
        for c in range(8):
            word_lst.append(arr[r][c])

        for i in range(8):
            word_lst2 = []
            for j in range(i, 8):
                word_lst2.append(word_lst[i])
                if word_lst2[j] == word_lst2[- 1 - j]:
                    if word_lst2 == word_lst2[::-1]:
                        if len(word_lst2) > max_len:
                            max_len = len(word_lst2)


    print(f'#{tc}', max_len)
