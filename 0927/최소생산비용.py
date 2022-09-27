def back(k):
    global visited, res, cur_sum

    if cur_sum >= res:
        return

    if k == n:
        res = min(cur_sum, res)
        return res

    for i in range(n):
        if i not in visited:
            visited[i] = 1
            cur_sum += arr[k][i]
            back(k+1)
            del visited[i]
            cur_sum -= arr[k][i]

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = 100000
    cur_sum = 0
    visited = {}
    back(0)
    print(f'#{tc} {res}')