arr = [ [ 1,  0,  0,  0,  0],
        [ 6,  7,  0,  0,  0],
        [11, 12, 13,  0,  0],
        [16, 17, 18, 19,  0],
        [21, 22, 23, 24, 25]]
N = 5
for r in range(N):
    for c in range(N):
        if r < c:
            print(arr[r][c])
# ============================
N = 5
for r in range(N - 1):
    for c in range(r + 1, N):
        print(arr[r][c])

# ======================
# 4개에서 3개를 선택
arr = 'abcd'
N = len(arr)

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            print(arr[i], arr[j], arr[k])
