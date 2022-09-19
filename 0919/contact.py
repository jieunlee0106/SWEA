for tc in range(1):
    n, s = map(int, input().split())
    lstt = list(map(int, input().split()))
    nums = [[0]]*101
    visited = [False]*101
    lst = []
    for i in range(0, n, 2):
        nums[lstt[i]].append(lstt[i+1])

    inn = [[0]*101]
    inn[0] = nums[s]
    idx = 1

    lst.append(s)

    while lst:
        s = lst.pop()
        for j in range(len(nums[s])):
            v = nums[s][j]
            if visited[v] == False:
                for p in range(len(nums[s])):
                    inn[idx].append(nums[s][p])
                lst.append(nums[s][j])
                visited[s] = True
            else: continue
        idx += 1

    print(inn)

