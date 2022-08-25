for t in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    new_arr = []
    cnt = 0

    # n극을 향하는 s극 버리기
    for c in range(n):
        for r in range(n):
            if arr[r][c] == 0 or arr[r][c] == 2:
                arr[r][c] = 0
            else:
                break

    # s극을 향하는 n극 버리기
    for c in range(n):
        for r in range(n-1, -1, -1):
            if arr[r][c] == 0 or arr[r][c] == 1:
                arr[r][c] = 0
            else:
                break

    # 0 제거하고 1or2인 숫자 리스트 만들기(new_arr)/ 인접한 두 수가 1,2이면 cnt += 1
    for c in range(100):
        new_arr = []
        for r in range(100):
            if arr[r][c] != 0:
                new_arr.append(arr[r][c])
        for i in range(1, len(new_arr)):
            if new_arr[i] == 2 and new_arr[i-1] == 1:
                cnt += 1

    print(f'#{t}', cnt)