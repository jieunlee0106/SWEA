T = int(input())

dx = [1, 1, -1, -1]
dy = [-1, 1, 1, -1]


def func():
    for length in range(N - 1, 1, -1):
        for i in range(1, length):
            j = length - i
            for r in range(i, N - j):
                for c in range(N - i - j):

                    visited = [False] * 101
                    y, x = r, c

                    for d in range(4):
                        n = j if d % 2 else i
                        for _ in range(n):
                            y, x = y + dy[d], x + dx[d]
                            if not visited[MAP[y][x]]:
                                visited[MAP[y][x]] = True
                            else:
                                break
                        else:
                            continue
                        break
                    else:
                        return length * 2

    return -1


for test_case in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    answer = func()

    print(f"#{test_case} {answer}")