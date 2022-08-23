cnt = 0
arr = [list([0]*100) for _ in range(100)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

for x in range(100):
    for y in range(100):
        if arr[x][y] == 1:
            cnt += 1
print(cnt)