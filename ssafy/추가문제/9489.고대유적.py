T = int(input())
for t in range(T):
    n, m = input().split()
    n = int(n)
    m = int(m)
    arr = [list(map(int, input().split())) for _ in range(n)]
    treasure_len = [] # arr[r][c] 지점의 사방의 1을 cnt 해서 넣을 리스트 =>  모든 구간에 대한 탐색이 끝나면 이 리스트에서 최댓값을 찾아서 출력할 것

    for r in range(n):
        for c in range(m):

            if arr[r][c] == 1: #어떤 지점의 값이 1일 때, 그 행의 모든 열을 순회하며 연속된 1의 개수를 찾는다.

                left_c = c
                right_c = c
                cnt = 1 #좌우 방향으로 연속된 1의 개수

                if c > 0 and arr[r][left_c-1] == 1: # 왼쪽에 1이 있을 때
                    while left_c > 0 and arr[r][left_c-1] == 1: # 왼쪽 방향으로 1이 연속해서 있을 때 cnt +=1
                        cnt += 1
                        left_c -= 1
                if c < m-1 and arr[r][right_c+1] == 1: #오른 쪽에 1이 있을 때
                    while right_c < m-1 and arr[r][right_c+1] == 1: # 오른쪽 방향으로 1이 연속해서 있을 때 cnt +=1
                        cnt += 1
                        right_c += 1
                treasure_len.append(cnt)

            if arr[r][c] == 1: #어떤 지점의 값이 1일 때, 그 열의 모든 행을 순회하며 연속된 1의 개수를 찾는다.

                up_r = r
                down_r = r
                cnt = 1 #상하 방향으로 연속된 1의 개수

                if r > 0 and arr[up_r-1][c] == 1: # 위쪽 방향으로 1이 연속해서 있을 때 cnt +=1
                    while up_r > 0 and arr[up_r-1][c] == 1:
                        cnt += 1
                        up_r -= 1
                if r < n-1 and arr[down_r+1][c] == 1: # 아래쪽 방향으로 1이 연속해서 있을 때 cnt +=1
                    while down_r < n-1 and arr[down_r+1][c] == 1:
                        cnt += 1
                        down_r += 1
                treasure_len.append(cnt)

    big_treasure = max(treasure_len)

    print(f'#{t+1}', big_treasure)

    ''' 
    cases = int(input())
 
for case in range(cases):
    N, M = map(int,input().split())
    table = [list(map(int,input().split())) for _ in range(N)]
 
    max_cnt = 0
    for i in range(N):
        r_cnt = 0
        for j in range(M):
            if table[i][j]:
                r_cnt += 1
                if max_cnt < r_cnt:
                    max_cnt = r_cnt
            else:
                r_cnt = 0
 
    for i in range(M):
        c_cnt = 0
        for j in range(N):
            if table[j][i]:
                c_cnt += 1
                if max_cnt < c_cnt:
                    max_cnt = c_cnt
            else:
                c_cnt = 0
 
    print(f'#{case+1}',max_cnt)
    '''