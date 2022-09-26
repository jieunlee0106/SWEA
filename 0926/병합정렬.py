def merge_sort(lst):
    global cnt

    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    l = merge_sort(lst[:mid])
    r = merge_sort(lst[mid:])
    if l[-1] > r[-1]:
        cnt += 1
    l_idx, r_idx = 0, 0
    ans = []
    while l_idx != len(l) and r_idx != len(r):
        if l[l_idx] <= r[r_idx]:
            ans.append(l[l_idx])
            l_idx += 1
        else:
            ans.append(r[r_idx])
            r_idx += 1
    if l_idx != len(l):
        ans.extend(l[l_idx:])
    if r_idx != len(r):
        ans.extend(r[r_idx:])
    return ans

for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    lst = list(merge_sort(arr))
    print(f'#{tc} {lst[n//2]} {cnt}')