
def back(lst, d):
    global cnt, b

    s = 0
    e = len(lst) - 1
    p = 0
    while s <= e:
        mid = (s + e) // 2

        if b >= lst[mid]:
            if b == lst[mid]:
                cnt += 1
                break
            s = mid + 1
            if p == 1: break
            p = 1

        elif b < lst[mid]:
            e = mid - 1
            if p == -1: break
            p = -1

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0

    for b in B:
        if b in A:
            d_lst = []
            back(A, 0)
        else:
            continue

    print(f'#{tc} {cnt}')