for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [input().rstrip('0') for _ in range(n)]
    nums = []
    pwd = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
        '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
        'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    pw_arr = []

    for r in range(n):
        if not arr[r]:
            continue
        else:
            if arr[r] not in pw_arr:
                pw_arr.append(arr[r])
                continue

    pw_len = len(pw_arr)

    for i in range(pw_len):
        pw = ''
        for j in pw_arr[i]:
            pw += pwd[j]
        pw = pw.rstrip('0')

        pwd2 = {
            '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
            '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

        zero_remove_pw = pw.lstrip('0')
        if (len(zero_remove_pw) + 3) // 112 < 1:

            e = len(pw) - 1

            for r in range(e - 55, e, 7):
                temp_pw = ''
                for i in range(r, r + 7):
                    temp_pw += pw[i]

                nums.append(pwd2[temp_pw])

            odd = nums[0] + nums[2] + nums[4] + nums[6]
            even = nums[1] + nums[3] + nums[5] + nums[7]
            result = odd * 3 + even
            if result % 10 == 0:
                print(f'#{tc} {sum(nums)}')


        else:
            pass  # 길이비가 1 : 2 이상일 때
