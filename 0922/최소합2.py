T = int(input())

dx = [0, 1]
dy = [1, 0]

def dfs(x, y):
    global res, tmp
    if res < tmp:  # 현재 결과값 보다 크면 함수 끝나도록 -> 제한시간때문에 가지치기 해야함
        return
    if x == N-1 and y == N-1:
        res = tmp
        return
    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        if (nx, ny) not in visited:
            visited.append((nx, ny))  # 좌표 업로드
            tmp += a[nx][ny]
            dfs(nx, ny)
            tmp -= a[nx][ny]  # 원상복구
            visited.remove((nx, ny))


for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    res = 3000
    tmp = a[0][0]
    dfs(0, 0)  # 현재좌표
    print("#{} {}".format(tc, res))


    for i in range(l):
        if not visited[i]:
            visited[i] = True
            lst.append(go[i])
            combi(k+1)
            lst.pop()
            visited[i] = False



for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dt = [(1, 0), (0, 1)]

    cur_sum = arr[0][0]
    # 이동 방향을 담음 리스트 만들기 / 1은 오른쪽 이동 / 2는 아래로 이동

    # n 이 3일 경우
    # go = ['d', 'd', 'r', 'r']

    go = [0]*2*(n-1)
    l = len(go)
    for i in range(n-1): go[i] = 1
    for i in range(n-1, l): go[i] = 2

    ans = []
    visited = [False] * l
    used = []
    lst = []
    ret = []

    combi(0)
    print(go)