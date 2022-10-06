
def back(k, cur_sum):
    global ans
    if cur_sum > n:
        return
    if k == n:
        if cur_sum == n:
            print(ans)
        return

    ans += [arr[k]]
    back(k + 1, cur_sum + arr[k])
    ans.pop()
    back(k + 1, cur_sum)




arr = [i for i in range(1, 11)]
n = 10
ans = []
back(0, 0)