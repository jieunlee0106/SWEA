def nqueen(row, visit):
    if row == n:
        global ans; ans += 1
        pass
    else:
        for col in range(n):
            if visit & (1 << col): continue # 같은 열은 제외
            a = row + col
            b = row - col + (n - 1)
            if line1[a] or line2[b]: continue   # 대각에 대해서 체크
            line1[a] = line2[b] = 1
            nqueen(row + 1, visit | (1 << col))
            line1[a] = line2[b] = 0
for i in range(1, 11):
    n = i
    ans = 0
    line1 = [0]*(n + n) # / = row + col
    line2 = [0]*(n + n) # \ = row - col + (n - 1)
    nqueen(0, 0)
    print(ans)