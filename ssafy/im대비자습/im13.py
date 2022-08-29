for t in range(1, int(input())+1):
    n = int(input())
    arr = [0]*5001
    n_list = []
    result = []
    for _ in range(n):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            arr[j] += 1

    p = int(input())
    for i in range(p):
        n_list.append(int(input()))
    for i in n_list:
        result.append(arr[i])
    print(f'#{t}', *result)