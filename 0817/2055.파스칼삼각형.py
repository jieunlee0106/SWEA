T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[1]+[0] * (N-1) for _ in range(N)]
    for i in range(1,N):  #모든 행에 대해서 수행
        for j in range(1, i+1):
            # i-1행의 j열과  j-1 열의 값 더해서 넣기
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j],end=' ')
        print()
