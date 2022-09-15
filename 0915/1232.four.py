for t in range(1, 11):
    n = int(input())
    node = [0]*(n+1)
    cal = []
    cal_n = []

    for i in range(n):
        lst = list(input().split())
        if lst[1] == '*' or lst[1] == '/' or lst[1] == '+' or lst[1] == '-' :
            cal.append(lst[1])
            cal_n.append(lst[2])
            cal_n.append(lst[0])
            cal_n.append(lst[3])

        else:
            node[int(lst[0])] = int(lst[1])

    for i in range(len(cal_n)-3, -1, -3):
        l, c, r = int(cal_n[i]), int(cal_n[i+1]), int(cal_n[i+2])
        if cal[-1] == '*':
            cal.pop()
            node[c] = node[l] * node[r]

        elif cal[-1] == '/':
            cal.pop()
            node[c] = int(node[l] / node[r])

        elif cal[-1] == '+':
            cal.pop()
            node[c] = node[l] + node[r]

        elif cal[-1] == '-':
            cal.pop()
            node[c] = node[l] - node[r]

    print(f'#{t}', node[1])