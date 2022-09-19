zo = list(map(int, '0000000111100000011000000111100110000110000111100111100111111001100111'))
cnt_lst = []
for p in range(0, len(zo), 7):
    n = []
    cnt = 0
    for i in range(p, p + 7):
        n.append(zo[i])

    if n[0] == 1:
       cnt += 64
    if n[1] == 1:
        cnt += 32
    if n[2] == 1:
        cnt += 16
    if n[3] == 1:
        cnt += 8
    if n[4] == 1:
        cnt += 4
    if n[5] == 1:
        cnt += 2
    if n[6] == 1:
        cnt += 1

    cnt_lst.append(cnt)
print(cnt_lst)
