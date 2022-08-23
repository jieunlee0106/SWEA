for t in range(1, int(input())+1):
    memory = list(map(int, input()))
    n = len(memory)

    if memory[0] == 0:
        ch_list = []
        for i in range(1, len(memory)):
            if memory[i] != memory[i-1]:
                ch_list.append(i)
        cnt = len(ch_list)
    else:
        ch_list = []
        for i in range(1, len(memory)):
            if memory[i] != memory[i-1]:
                ch_list.append(i)
        cnt = len(ch_list)+1
    print(f'#{t}', cnt)
