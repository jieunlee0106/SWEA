
T = int(input())


for t in range(T):
    l = list(input().split())
    sn = l[0]
    n = int(l[1])
    nums = list(input().split())
    num_p = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    new_nums =[]
    for j in range(10):
        for i in range(n):
            if nums[i] == num_p[j]:
                 new_nums.append(nums[i])
            else:
                continue

    print(f'#{t+1}', *new_nums)




