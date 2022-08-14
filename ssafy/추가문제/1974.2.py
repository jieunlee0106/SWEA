T = int(input())

for t in range(T):
    result = 1
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        if i == 0 or i == 3 or i == 6:
            block_n = []
            for r in range(i, i + 3):
                for c in range(i, i + 3):
                    if puzzle[r][c] not in block_n:
                        block_n.append(puzzle[r][c])
                    else:
                        result = 0
                        break
        for r in range(i, 9):
            c_line_n = []
            for c in range(i, 9):
                if puzzle[r][c] not in c_line_n:
                    c_line_n.append(puzzle[r][c])
                else:
                    result = 0
                    break
        for c in range(i, 9):
            r_line_n = []
            for r in range(i, 9):
                if puzzle[r][c] not in r_line_n:
                    r_line_n.append(puzzle[r][c])
                else:
                    result = 0
                    break

    print(f'#{t+1}', result)