for t in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    # 3x3 배열 검사

    for i in range(0, 9, 3):
        if result == 0:
            break
        for j in range(0, 9, 3):
            already_s = []
            if result == 0:
                break
            for r in range(i, i+3):
                if result == 0:
                    break
                for c in range(j, j+3):
                    if arr[r][c] not in already_s:
                        already_s.append(arr[r][c])
                    else:
                        result = 0
                        break

    # 가로줄 세로줄 검사
    for r in range(9):
        already_r = []
        already_c = []
        if result == 0:
            break
        for c in range(9):
            if arr[r][c] not in already_r:
                already_r.append(arr[r][c])

            elif arr[r][c] in already_r:
                result = 0
                break

            if arr[c][r] not in already_c:
                already_c.append(arr[c][r])

            elif arr[r][c] in already_c:
                result = 0
                break

    print(f'#{t}', result)