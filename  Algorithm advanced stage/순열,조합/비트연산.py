arr = [1,2,3]
result = []

for i in range(1<<len(arr)):
    subset = []
    for j in range(len(arr)):
        if i & (1<<j):
            subset.append(arr[j])
    result.append(subset)
print(result)
# 1 << n 의 의미하는건 2진수 비트 1을 n만큼 왼쪽으로 이동 시키라는 의미
# 000001 이 왼쪽으로 두번 이동하면 00100 16이 된다
# n 이 4이면 i의 범위는 0 ~ 15
