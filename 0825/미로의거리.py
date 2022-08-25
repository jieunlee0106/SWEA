for t in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[0]*(n) for _ in range(n)]
    q = []

    #시작 좌표, 끝 좌표 구하기
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 3:
                end_r = r
                end_c = c
            elif arr[r][c] == 2:
                start_r = r
                start_c = c
    sr = start_r
    sc = start_c

    def bfs(sr, sc, end_r, end_c):
        q.append([sr, sc])
        visited[sr][sc] = 0
        while q:
            sr, sc = q[0][0], q[0][1]
            for r in range(n):
                for c in range(n):
                    if sr-1 >= 0 and arr[q[0][0]-1][q[0][1]] == 0:
                        if not visited[sr-1][sc]:
                            q.append([sr-1][sc])
                            sr = sr-1
                            visited[sr][sc] += 1
                    if sr+1 < n and arr[q[0][0]+1][q[0][1]] == 0:
                        if not visited[sr+1][sc]:
                            q.append([sr+1][sc])
                            sr = sr+1
                            visited[sr][sc] += 1
                    if sc-1 >= 0 and arr[q[0][0]][q[0][1]-1] == 0:
                        if not visited[sr][sc-1]:
                            q.append([sr][sc-1])
                            sc = sc-1
                            visited[sr][sc] += 1
                    if sc+1 < n and arr[q[0][0]][q[0][1]+1] == 0:
                        if not visited[sr][sc+1]:
                            q.append([sr][sc+1])
                            sc = sc-1
                            visited[sr][sc] += 1

                            if sr == end_r and sc == end_c:
                                return visited[sr][sc]
                return 0

    print(bfs(sr, sc, end_r, end_c))