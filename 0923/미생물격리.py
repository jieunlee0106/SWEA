# 두개 이상의 군집이 합쳐질 때 방향을 결정하는 함수
def merge():
    pass

# 군집이 시약에 위치했을 때
def reagent(cnt, di):
    pass
    cnt = cnt // 2

    if di == 1:
        di = 2
    elif di == 2:
        di = 1
    elif di == 3:
        di = 4
    elif di == 4:
        di = 3
    return cnt, di


# 군집 이동 함수
def go(r, c, cnt, di):
    r += dr[di]
    c += dc[di]

    if (r != 0 or r != n - 1) or (c != 0 or c != n - 1):
        cnt, di = reagent(cnt, di)
    else:pass

for tc in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(k)]

    # 0번 인덱스는 사용안함 / 상 하 좌 우
    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]

    for t in range(m):
        for i in range(k):
            r, c, cnt, di = arr[i][0], arr[i][1], arr[i][2], arr[i][3]
            arr[i] = list(go(r, c, cnt, di))

        d = {}
        merge_lst = [[]*k for _ in range(k)]

        for j in range(k):
            rr, cc = arr[j][0], arr[j][1]
            if (rr, cc) not in d:
                d[(rr, cc)] = 1
                merge_lst[j].append()
            else:
                pass