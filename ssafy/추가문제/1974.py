T = int(input())

for t in range(T):
    result = 1
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        if i == 0 or i == 3 or i == 6:
            if puzzle[i][i] != puzzle[i][i+1] != puzzle[i][i+2] != puzzle[i+1][i] != puzzle[i+1][i+1] != puzzle[i+1][i+2] != puzzle[i+2][i] != puzzle[i+2][i+1] != puzzle[i+2][i+2] :
                result = 1
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