def PAY(bill, idx, p):
    global pay, cur_pay

    if bill > cur_pay:
        return

    if p == cnt:
        cur_pay = min(bill, cur_pay)
        return

    for s in range(idx, 12):
        if month[s] != 0:
            for i in ['DAY', 'MON', 'T_MON']:
                if i == 'DAY':
                    PAY(bill + (month[s] * d), s + 1, p + 1)

                elif i == 'MON':
                    PAY(bill + m, s + 1, p + 1)

                elif i == 'T_MON':
                    k = month[s:s+3].count(0)
                    PAY(bill + tm, s + 3, p + 3 - k)

for tc in range(1, int(input())+1):
    d, m, tm, y = map(int,input().split())
    month = list(map(int, input().split()))
    month += [0, 0, 0]
    # 연 월 일 3월 권 중 하나만 사용ㅎ나 경우 넣기
    pay = [y, sum(month)*d]

    cnt = 0
    last_swim = 0
    for i in range(12):
        if month[i] != 0:
            cnt += 1
            last_swim = i
    pay += [cnt * m]

    cur_pay = min(pay)
    PAY(0, 0, 0)

    print(f'#{tc}', cur_pay)