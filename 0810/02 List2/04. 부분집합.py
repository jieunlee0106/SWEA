# 바이너리 카운팅

arr = [i for i in range(1, 5)]
N = len(arr)

# 원소수가 N인 집합의 모든 부분집합에 대응하는 10진수 => 0 ~ (2^n - 1)
for subset in range(0, 1 << N):
    # subset의 N개의 bit를 조사
    S = cnt = 0
    for i in range(N):  # N => 0 ~ 3
        if subset & (1 << i):
            print(arr[i], end=' ')
            S += arr[i]
            cnt += 1
    print(f'===> 합={S}')