def b(k, cur_sum):
    global ans
    if cur_sum > hap:
        return
    if k == n :
        if cur_sum == hap:
           ans += 1
        return
    b(k+1, cur_sum + arr[k])
    b(k+1, cur_sum)

for tc in range(1, int(input())+1):
    n ,hap = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    b(0, 0)
    print(f'#{tc} {ans}')