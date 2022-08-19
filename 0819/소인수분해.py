T = int(input())

for t in range(T):
    num_list = []
    nums = int(input())
    if nums != 1:
        while nums % 10 == 0:
            num_list.append(2)
            num_list.append(5)
            nums = nums/10
        while nums % 2 == 0:
            num_list.append(2)
            nums = nums/2
        while nums % 3 == 0:
            num_list.append(3)
            nums = nums/3
        while nums % 5 == 0:
            num_list.append(5)
            nums = nums/5
        while nums % 7 == 0:
            num_list.append(7)
            nums = nums/7
        while nums % 11 == 0:
            num_list.append(11)
            nums = nums/11
        while nums / 1 == 1:
            break

    a, b, c, d, e = 0, 0, 0, 0, 0

    for i in num_list:
        if i == 2:
            a += 1
        elif i == 3:
            b += 1
        elif i == 5:
            c += 1
        elif i == 7:
            d += 1
        elif i == 11:
            e += 1

    print(f'#{t+1}', a, b, c, d, e)