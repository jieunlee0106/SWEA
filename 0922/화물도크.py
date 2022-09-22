def back(idx, end, cnt):
    global ret
    for j in range(idx+1, n):
        if end <= lst[j][0]:
            end = lst[j][1]
            idx = j
            cnt += 1
    ret =  max(cnt, ret)
    return ret

for tc in range(1, int(input())+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst.sort(key=lambda x: x[1])

    cnt_lst = []
    ret = 0
    for i in range(n):
        end = lst[i][1]
        idx = i
        cnt_lst.append(back(idx, end, 1))

    print(f'#{tc} {ret}')