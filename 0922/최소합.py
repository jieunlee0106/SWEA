# 이동 방향을 담는 리스트 만들기/  2차원 배열 한 변의 길이가 n 이면
'''
이동 방향은 오른쪽, 아래 방향으로 각 n-1 씩 이동 할 수 있다.
이동 방향 리스트 => 길이가  2*(n-1)인 go 에 오른 쪽으로 이동 할 때 1 / 아래로 이동 할 때 2 를 넣어준 go 리스트를 만들다
예시 1번 n = 3 일 때, [1, 1, 2, 2]
리스트에 따라 배열이 이동하며 숫자를 더해주는 방식
가지치기 - 중복된 go는 가지 않기 (used 딕셔너리 사용) / 배열을 따라 이동 하다가 그 전에 구했던 최소값 보다 커지면 계산 끝내기
'''


def back(lst, k, r, c, cur_sum):
    global ret
    if k == l:

        s = ''.join(map(str, lst))
        if s not in d:
            d[s] = 1

            for g in range(l):
                if lst[g] == 1:
                    R = r + dt[1][0]
                    C = c + dt[1][1]

                    cur_sum += arr[R][C]
                    r = R
                    c = C

                    if ret <= cur_sum:
                        return

                else:
                    R = r + dt[0][0]
                    C = c + dt[0][1]

                    cur_sum += arr[R][C]
                    r = R
                    c = C

                    if ret <= cur_sum:
                        return

            ret = min(ret, cur_sum)

            cur_sum = arr[0][0]

            return

    for j in range(l):
        if not visited[j]:
            visited[j] = 1
            lst.append(go[j])
            back(lst, k+1, r, c, cur_sum)
            lst.pop()
            visited[j] = 0
    return

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dt = [(1, 0), (0, 1)]

    ans = []
    # 이동 방향을 담음 리스트 만들기 / 1은 오른쪽 이동 / 2는 아래로 이동
    go = [0]*2*(n-1)
    l = len(go)
    visited = [0]*l
    for i in range(n-1):
        go[i] = 1
    for i in range(n-1, len(go)):
        go[i] = 2

    su_lst = []
    cur_sum = arr[0][0]
    ret = 100
    used = []
    d = {}
    back([], 0, 0, 0, cur_sum)
    print(f'#{tc} {ret}')

