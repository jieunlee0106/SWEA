
T = int(input())
for t in range(T):
    n = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for i in range(n):

        color_arr = list(map(int, input().split()))
        for r in range(len(arr)):
            for c in range(len(arr)):
                if color_arr[0] <= r <= color_arr[2] and color_arr[1] <= c <= color_arr[3] :
                    if arr[r][c] == 0:
                        arr[r][c] += color_arr[4]
                    elif arr[r][c] == color_arr[4]:
                        arr[r][c] = color_arr[4]
                    elif arr[r][c] != color_arr[4]:
                        arr[r][c] = 3 #  보라색은 3

    purple = 0
    for r in range(len(arr)):
        for c in range(len(arr)):
            if arr[r][c] == 3:
                purple += 1

    print(f'#{t+1}', purple)
