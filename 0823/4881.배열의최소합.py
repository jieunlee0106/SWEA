'''
for t in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cols = [i for i in range(n)] # [0, 1, ... , n-1]

    def perm(k):
        if k == n:
            s= 0
            for i in range(n):
                s += arr[i][cols[i]]
            print(cols, s)
        else:
            for i in range(k, n):
                cols[k], cols[i] = cols[i], cols[k]
                perm(k+1)
                cols[k], cols[i] = cols[i], cols[k]
    perm(0)

'''

#가지치기
#가지치기의 가장 단순한 개념,

for t in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cols = [i for i in range(n)] # [0, 1, ... , n-1]
# 마지막에 구한 합이 아니라 , 그때 그때 마다의 합을 알 수 있어, 가다가 최솟값보다 커지면 끊어
    def perm(k, cur_sum):
        global ans
        if cur_sum >= ans:
            return

        if k == n:
            s = 0
            for i in range(n):
                s += arr[i][cols[i]]
            # print(cols, s, cur_sum)
            if ans > s:
                ans = s
        else:
            for i in range(k, n):
                cols[k], cols[i] = cols[i], cols[k]
                perm(k+1, cur_sum + arr[k][cols[k]])
                cols[k], cols[i] = cols[i], cols[k]

    ans = 0xffffffff
    perm(0, 0)
    print(f'#{t}', ans)