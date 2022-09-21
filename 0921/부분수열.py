def dfs(k):
    if k == n:
        pass
    else:
        for i in range(n):
            dfs(k+1)

dfs(0)

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    ans = []
    cnt = 0
    print(dfs(cnt))
