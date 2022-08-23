N = int(input())

arr = [list([0]*1001) for _ in range(1001)]
for n in range(1, N+1):
    dc, dr, w, h = map(int, input().split())
    for c in range(dc, dc+w):
        for r in range(dr, dr+h):
            arr[r][c] = n
    cnt_list = []
for k in range(1, N+1):
    cnt = 0
    for r in range(1001):
        for c in range(1001):
            if arr[r][c] == k:
                cnt += 1
    cnt_list.append(cnt)

print(*cnt_list, sep='\n')