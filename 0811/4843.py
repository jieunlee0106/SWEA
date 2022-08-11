T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    special_list = []
    for j in range(N, 0, -1):
        for i in range(1, j):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
    for i in range(10):
        if i% 2 == 1:
            special_list.append(nums.pop(0))
        else:
            special_list.append(nums.pop(-1))
    print(f'#{t+1}', *special_list)