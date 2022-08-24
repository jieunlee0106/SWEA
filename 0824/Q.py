def password(list):
    while True:
        for i in range(1, 6):  # 1, 2, 3, 4, 5
            num = list.pop(0)  # 맨 처음 숫자를 빼
            list.append(num - i)  # 이 숫자를 i만큼 빼고, 맨 뒤에 넣어줘

            # 0이 나오면
            if list[-1] <= 0:  # 가장 마지막 값이 0보다 작거나 같으면
                list[-1] = 0   # 0
                return list

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    numbers = list(map(int, input().split())) # [9550, 9556, 9550, 9553 9558 9551 9551 9551]

    result = password(numbers)
    # print('#{}'.format(tc), ' '.join(map(str, (result))))
    print('#{}'.format(tc), *result)