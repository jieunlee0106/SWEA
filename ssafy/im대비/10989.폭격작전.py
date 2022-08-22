for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0   #피해입은 적군 수
    overlap_r_c = [] #좌표가 다른 좌표랑 겹치는지 확일 할 리스트
    for _ in range(m):
        arr_r, arr_c, l = map(int, input().split())
        for r in range(arr_r-l, arr_r+l+1):
            if 0 <= r < n:
                if [r, arr_c] not in overlap_r_c:
                    cnt += arr[r][arr_c]
                    overlap_r_c.append([r, arr_c])

        for c in range(arr_c-l, arr_c+l+1):
            if 0 <= c < n:
                if [arr_r, c] not in overlap_r_c:
                    cnt += arr[arr_r][c]
                    overlap_r_c.append([arr_r, c])

    print(f'#{t}', cnt)
