T = int(input())

for t in range(T):
    words = [list(input()) for _ in range(5)]
    new_word = []
    max_len = len(words[0])
    for il in range(len(words)):
        if len(words[il]) > max_len:
            max_len = len(words[il])

    for i in range(len(words)):
        if len(words[i]) < max_len:
            for l in range(max_len - len(words[i])):
                words[i].append('.')

    for r in range(max_len):
        for c in range(5):
            if words[c][r] != '.':
                new_word.append(words[c][r])

    new_words = ''.join(new_word)
    print(f'#{t+1}', new_words)
