for tc in range(1, int(input())+1):
    n, m, k = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(k)]

    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]
    rd = [0, 2, 1, 4, 3]


    for _ in range(m):
        dic = {}
        for i in range(k):
            r, c, num, di = arr[i]

            if k ==0 :continue

            nr = r + dr[di]
            nc = c + dc[di]
            arr[i][0] = nr
            arr[i][1] = nc

            if not (1 <= nr < n-1 and 1 <= nc < n-1):
                arr[i][2] //= 2
                arr[i][3] = rd[di]

            if (nr, nc) not in dic.keys():
                dic[(nr, nc)] = [i, num]

            else:
                idx, size = dic[(nr, nc)]
                if arr[i][2] > size:
                    dic[(nr, nc)] = [i, arr[i][2]]
                    arr[i][2] += arr[idx][2]
                    arr[idx][2] = 0
                else:

                    arr[idx][2] += arr[i][2]
                    arr[i][2] = 0
    ret = 0
    for j in range(k):
        ret += arr[j][2]
    print(f'#{tc} {ret}')

