for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    plus = 0
    overlap_r_c = [] #더해지는 r,c 의 좌표를 넣을 리스트, 이 리스트 안에 있는 좌표가 또 나오면 그 수는 다시(두번)세지 않는다.
    for _ in range(m):
        l_u, c_u, l = map(int, input().split()) #좌상단
        l_d, c_d = l_u + l-1, c_u + l-1 #우하단
        for r in range(l_u, l_d+1):
            for c in range(c_u, c_d+1):
                if r < n and c < n: #arr 범위 내에 있는 좌표의 수만 더하기
                    if [r, c] not in overlap_r_c: # m*m 행렬 중 다른 m*m과 겹치는 부분이 있으면 또 더하지 않기
                        plus += arr[r][c]
                        overlap_r_c.append([r, c])
    print(f'#{t}', plus)