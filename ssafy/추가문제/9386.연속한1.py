for t in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input()))
    cnt = 1
    cnt_list = []
    for i in range(n):
        if i != 0:
            if nums[i] == 1 and nums[i-1] == 1:
                cnt += 1
                cnt_list.append(cnt)
            elif nums[i-1] == 1 and nums[i] == 0:
                cnt = 1
    if not cnt_list:
        print(f'#{t}', 1)
    else:
        print(f'#{t}', max((cnt_list)))