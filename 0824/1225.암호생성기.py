for _ in range(10):
    t = int(input())
    arr = list(map(int, input().split()))
    idx = -1
    cnt = 0
    while arr[idx] > 0:
        idx += 1
        idx = idx % 8
        arr[idx] -= cnt % 5 + 1
        cnt += 1
    arr[idx] = 0
    answer = arr[idx+1:] + arr[:idx+1]
    print(f'#{t}', *answer)