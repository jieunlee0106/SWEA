for tc in range(1, 2):
    n, start = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = [[] for _ in range(102)]
    level = [[] for _ in range(102)]

    for i in range(0, n, 2):
        tree[lst[i]] += [lst[i+1]]
    visited = [start]
    level[0] = start
    le = 1
    level[le] += tree[start]
    stack = level[le]

    while level[le]:
        while stack:
            start = stack.pop()
            if start not in visited:
                visited.append(start)
                level[le] += tree[start]
        stack = level[le]
        le += 1
    print(max(level[le-1]))