from collections import deque
def bfs(c):
    k = 1
    while c != 1:
        for j in range(1, v+1):
            if c == 1:
                break
            if graph[0][j] == c or graph[1][j] == c:
                c = j
                if c not in ans:
                    ans.append(c)
                    break
                else:
                    k = c
                    return k
    return k

def bfs2(val):
    cnt= 0
    while q:
        cnt += 1
        if graph[0][val] != 0:
            q.append(graph[0][val])
        if graph[1][val] != 0:
            q.append(graph[1][val])
        q.popleft()
        if not q:
            break
        val = q[0]
    return cnt

for t in range(1, int(input())+1):
    v, e, n1, n2 = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = [[0]*(v+1) for _ in range(2)]

    for i in range(0, e*2, 2):
        if graph[0][lst[i]] == 0:
            graph[0][lst[i]] = lst[i + 1]
        else:
            graph[1][lst[i]] = lst[i + 1]

    ans = []
    bfs(n1)
    k = bfs(n2)

    q = deque()
    q.append(k)

    print(f'#{t}', k, bfs2(k))
