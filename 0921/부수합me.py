def back(deep, cur_sum):
    global ans
    if cur_sum > m:
        return
    if deep == n:
        if cur_sum == m:
           ans += 1
        return
    back(deep+1, cur_sum + lst[deep])
    back(deep+1, cur_sum)


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0
    deep = 0
    cur_sum = 0
    back(deep, cur_sum)
    print(f'#{tc} {ans}')