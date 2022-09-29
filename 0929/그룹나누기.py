def find_set(x):
    while x != N[x]:
        x = N[x]
    else:
        return x
def union(x, y):
    N[find_set(y)] = find_set(x)

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    N = [i for i in range(n+1)]
    lst = list(map(int, input().split()))
    for i in range(0, m*2, 2):
        s, e = lst[i], lst[i+1]
        if find_set(s) != find_set(e):
            union(s, e)
            n -= 1

    print(f'#{tc} {n}')
# N 이 바뀌지는 않음
