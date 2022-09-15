from collections import deque
for t in range(int(input())):
    e, root = map(int, input().split())
    graph = [[0]*2 for _ in range(e+2)]
    lst = list(map(int, input().split()))
    for i in range(0, e*2, 2):
        p, c = lst[i], lst[i+1]
        if graph[p][0] == 0:
            graph[p][0] = c
        else:
            graph[p][1] = c

    q = deque()
    q.append(graph[root][0])
    q.append(graph[root][1])
    cnt = 1

    def bfs():
        global cnt
        while q:
            if q[0] != 0:
                cnt += 1
                root = q.popleft()
                q.append(graph[root][0])
                q.append(graph[root][1])
            else:
                q.popleft()
        return cnt
    result = bfs()
    print(f'# {t+1}', result)
