for t in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    result = 'NO'
    # 행과 열에서 오목인 경우 찾기
    for j in range(n - 4):
        for i in range(n - 4):
            if result == 'YES':
                break
            for r in range(i, i + 5):
                r_cnt = 0
                c_cnt = 0
                if result == 'YES':
                    break
                for c in range(j, j + 5):
                    if arr[r][c] == 'o':
                        r_cnt += 1
                    if arr[c][r] == 'o':
                        c_cnt += 1
                if r_cnt == 5 or c_cnt == 5:
                    result = 'YES'
    # 대각선으로 5개 연속으로 오목인 경우 찾기
    if result == 'NO':
        for j in range(n - 4):
            for i in range(n - 4):
                x_list = []
                if result == 'YES':
                    break
                for r in range(i, i + 5):
                    for c in range(j, j + 5):
                        x_list.append(arr[r][c])
                if x_list[0] == 'o' and x_list[6] == 'o' and x_list[12] == 'o' and x_list[18] == 'o' and x_list[
                    24] == 'o':
                    result = 'YES'
                elif x_list[4] == 'o' and x_list[8] == 'o' and x_list[12] == 'o' and x_list[16] == 'o' and x_list[
                    20] == 'o':
                    result = 'YES'

    print(f'#{t}', result)