def PAY_M(bill, idx, p):                            # 한달권이 포함된 리스트
    global pay, cur_pay, iidx
    if bill > cur_pay:
        return

    if idx + 1 == iidx:
        cur_pay = min(bill, cur_pay)

        return

    for s in range(p, 12):
        if month[s] != 0:
            for i in ['DAY', 'MON']:                  # 0 이면 일일권 , 1이면 월권
                if i == 'DAY':
                    PAY_M(bill + (month[s] * d), idx + 1, s + 1)

                elif i == 'MON':
                    PAY_M(bill + m, idx + 1, s + 1)


def PAY_TM(bill, idx, p):
    global pay, cur_pay
    if bill > cur_pay:
        return

    if idx + 1 == iidx:
        cur_pay = min(bill, cur_pay)

        return

    for s in range(p, 12):
        if month[s] != 0:
            for i in ['DAY', 'MON', 'T_MON']:  # 0 이면 일일권 , 1이면 월권
                if i == 'DAY':
                    PAY_M(bill + (month[s] * d), idx + 1, s + 1)

                elif i == 'MON':
                    PAY_M(bill + m, idx + 1, s + 1)

                elif i == 'T_MON':
                    PAY_TM(bill + tm, idx + 3, s + 3)


for tc in range(1, int(input())+1):
    d, m, tm, y = map(int,input().split())
    month = list(map(int, input().split()))

    # 연 월 일 3월 권 중 하나만 사용ㅎ나 경우 넣기
    pay = [y, sum(month)*d]

    cnt = 0
    iidx = 0
    for i in month:
        if i != 0:
            cnt += 1
            iidx = i
    pay += [cnt * m]

    mm = 0
    mmm = []

    # 3달 이용권만 구매하는 경우
    for i in range(10):
        if month[i] != 0 and i not in mmm:
            mm += 1
            mmm += [i, i+1, i+2]
    pay += [mm * tm]
    pay = [min(pay)]
    cur_pay = min(pay)

    k = 0
    PAY_M(0, 0, 0)
    PAY_TM(cur_pay, 0, 0)
    print(cur_pay)