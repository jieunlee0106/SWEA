for tc in range(1, 11):
    n, start = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = [[] for _ in range(102)]
    level = [[] for _ in range(102)]
    stack = []
    for i in range(0, n, 2):
        tree[lst[i]] += [lst[i+1]]
    visited = {}
    visited[start] = 1
    level[0] = [start]
    le = 1
    level[le] += tree[start]
    stack.extend(level[le])

    while level[le]:
        le += 1
        while stack:
            start = stack.pop()
            if start not in visited:
                visited[start] = 1
                for j in range(len(tree[start])):
                    if tree[start][j] not in visited:

                        level[le].append(tree[start][j])
        stack.extend(level[le])

    print(f'#{tc} {max(level[le-1])}')