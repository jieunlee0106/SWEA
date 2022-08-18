T = int(input())
for t in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    n_nums = []
    for i in range(n):
        if nums[i] == 0:
            n_nums.pop()
        else:
            n_nums.append(nums[i])
    print(f'#{t+1}', sum(n_nums))

