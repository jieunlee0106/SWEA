for _ in range(10):
    t = int(input())
    n = 16
    arr = [list(map(int, input())) for _ in range(n)]

    for r in range(n):
        for c in range(n):
            if arr[r][c] == 3:
                end_r = r
                end_c = c
            elif arr[r][c] == 2:
                start_r = r
                start_c = c

    sr = start_r
    sc = start_c
    stack = []
    result = 1
    aready = []  #stack에서 이미 사용되고 pop된 좌표 넣는 리스트

    while sr != end_r or sc != end_c:

        if sr == end_r and sc == end_c:
            result = 1
            break
        elif sr != end_r or sc != end_c:
            if 0 <= sc-1 and (arr[sr][sc-1] == 0 or arr[sr][sc-1] == 3) and [sr, sc-1] not in aready:
                stack.append([sr, sc-1])
            if sc+1 < n and (arr[sr][sc+1] == 0 or arr[sr][sc+1] == 3) and [sr, sc+1] not in aready:
                stack.append([sr, sc + 1])
            if 0 <= sr-1 and (arr[sr-1][sc] == 0 or arr[sr-1][sc] == 3) and [sr-1, sc] not in aready:
                stack.append([sr-1 , sc])
            if sr+1 < n and (arr[sr+1][sc] == 0 or arr[sr+1][sc] == 3) and [sr+1, sc] not in aready:
                stack.append([sr+1, sc])
            if stack:
                sr, sc = stack[-1][0], stack[-1][1]
                aready.append(stack.pop())
            elif not stack:
                result = 0
                break

        else:
            result = 0
            break

    print(f'#{t}', result)