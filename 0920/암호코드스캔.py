import sys; sys.stdin = open('2117.txt')
for tc in range(1, int(input())+1):
    nlst = [0]*21
    n, m = map(int, input().split())
    arr = [input().rstrip('0') for _ in range(n)]
    nums = []
    end_of_verification = []
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
        nums = []
        pw = ''
        if end_of_verification:
            for v in end_of_verification:

                if pw_arr[i] in v or v in pw_arr[i]:
                    pw_arr[i] = pw_arr[i].replace(v, '').rstrip('0')
                    end_of_verification.append(pw_arr[i].lstrip('0'))
                    break
                else:
                    end_of_verification.append(pw_arr[i].lstrip('0'))
                    break
        else:
            end_of_verification.append(pw_arr[i].lstrip('0'))

        for j in pw_arr[i]:
            pw += pwd[j]

        pw = pw.rstrip('0')

        pwd2 = {
            '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
            '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

        zero_remove_pw = pw_arr[i].lstrip('0')

        if len(pw_arr[i].lstrip('0'))*4 // 7 <= 8:

            e = len(pw) - 1

            for r in range(e-55, e, 7):
                temp_pw = ''
                for o in range(r, r+7):
                    temp_pw += pw[o]

                nums.append(pwd2[temp_pw])

            odd = nums[0] +nums[2] +nums[4] +nums[6]
            even = nums[1] +nums[3] +nums[5] +nums[7]
            result = odd*3 + even
            if result % 10 == 0:
                nlst[tc] += sum(nums)
            else:
                pass
        else:
            if len(pw_arr[i].lstrip('0'))*4 // 7 <= 16:
                pwd2 = {
                    '00000011110011': 0, '00001111000011': 1, '00001100001111': 2, '00111111110011': 3, '00110000001111': 4,
                    '00111100000011': 5, '00110011111111': 6, '00111111001111': 7, '00111100111111': 8, '00000011001111': 9}

                e = len(pw) - 1

                for r in range(e-(56)*2+1, e, 14):
                    temp_pw = ''
                    for o in range(r, r+14):
                        temp_pw += pw[o]

                    nums.append(pwd2[temp_pw])

                odd = nums[0] +nums[2] +nums[4] +nums[6]
                even = nums[1] +nums[3] +nums[5] +nums[7]
                result = odd*3 + even

                if result % 10 == 0:
                    nlst[tc] += sum(nums)

            elif len(pw_arr[i].lstrip('0'))*4 // 7 <= 24:
                pwd2 = {
                    '000000000111111000111': 0, '000000111111000000111': 1, '000000111000000111111': 2, '000111111111111000111': 3, '000111000000000111111': 4,
                    '000111111000000000111': 5, '000111000111111111111': 6, '000111111111000111111': 7, '000111111000111111111': 8, '000000000111000111111': 9}

                e = len(pw) - 1

                for r in range(e - (56)* 3 + 1, e, 21):
                    temp_pw = ''
                    for o in range(r, r + 21):
                        temp_pw += pw[o]

                    nums.append(pwd2[temp_pw])

                odd = nums[0] + nums[2] + nums[4] + nums[6]
                even = nums[1] + nums[3] + nums[5] + nums[7]
                result = odd * 3 + even

                if result % 10 == 0:
                    nlst[tc] += sum(nums)

            elif len(pw_arr[i].lstrip('0'))*4 // 7 <= 32:
                pwd2 = {
                    '0000000000001111111100001111': 0, '0000000011111111000000001111': 1, '0000000011110000000011111111': 2, '0000111111111111111100001111': 3, '0000111100000000000011111111': 4,
                    '0000111111110000000000001111': 5, '0000111100001111111111111111': 6, '0000111111111111000011111111': 7, '0000111111110000111111111111': 8, '0000000000001111000011111111': 9}


                e = len(pw) - 1

                for r in range(e - (56)* 4 + 1, e, 28):
                    temp_pw = ''
                    for o in range(r, r + 28):
                        temp_pw += pw[o]

                    nums.append(pwd2[temp_pw])

                odd = nums[0] + nums[2] + nums[4] + nums[6]
                even = nums[1] + nums[3] + nums[5] + nums[7]
                result = odd * 3 + even

                if result % 10 == 0:
                    nlst[tc] += sum(nums)

            elif len(pw_arr[i].lstrip('0'))*4 // 7 <= 40:
                pwd2 = {
                    '00000000000000011111111110000011111': 0, '00000000001111111111000000000011111': 1, '00000000001111100000000001111111111': 2, '00000111111111111111111110000011111': 3, '00000111110000000000000001111111111': 4,
                    '00000111111111100000000000000011111': 5, '00000111110000011111111111111111111': 6, '00000111111111111111000001111111111': 7, '00000111111111100000111111111111111': 8, '00000000000000011111000001111111111': 9}

                e = len(pw) - 1

                for r in range(e - (56)* 5 + 1, e, 35):
                    temp_pw = ''
                    for o in range(r, r + 35):
                        temp_pw += pw[o]

                    nums.append(pwd2[temp_pw])

                odd = nums[0] + nums[2] + nums[4] + nums[6]
                even = nums[1] + nums[3] + nums[5] + nums[7]
                result = odd * 3 + even

                if result % 10 == 0:
                    nlst[tc] += sum(nums)


            elif len(pw_arr[i].lstrip('0'))*4 // 7 <= 48:

                pwd2 = {
                    '000000000000000000111111111111000000111111': 0, '000000000000111111111111000000000000111111': 1, '000000000000111111000000000000111111111111': 2, '000000111111111111111111111111000000111111': 3, '000000111111000000000000000000111111111111': 4,
                    '000000111111111111000000000000000000111111': 5, '000000111111000000111111111111111111111111': 6, '000000111111111111111111000000111111111111': 7, '000000111111111111000000111111111111111111': 8, '000000000000000000111111000000111111111111': 9}

                e = len(pw) - 1

                for r in range(e - (56)* 6 + 1, e, 42):
                    temp_pw = ''
                    for o in range(r, r + 42):
                        temp_pw += pw[o]

                    nums.append(pwd2[temp_pw])

                odd = nums[0] + nums[2] + nums[4] + nums[6]
                even = nums[1] + nums[3] + nums[5] + nums[7]
                result = odd * 3 + even

                if result % 10 == 0:
                    nlst[tc] += sum(nums)

            elif len(pw_arr[i].lstrip('0'))*4 // 7 <= 56:
                pwd2 = {
                    '000000000000000000000111111111111110000001111111': 0, '0000000000000011111111111111000000000000001111111': 1, '0000000000000011111110000000000000011111111111111': 2, '0000000111111111111111111111111111100000001111111': 3, '0000000111111100000000000000000000011111111111111': 4,
                    '0000000111111111111110000000000000000000001111111': 5, '0000000111111100000001111111111111111111111111111': 6, '0000000111111111111111111111000000011111111111111': 7, '0000000111111111111110000000111111111111111111111': 8, '0000000000000000000001111111000000011111111111111': 9}

                e = len(pw) - 1

                for r in range(e - (56)* 7 + 1, e, 49):
                    temp_pw = ''
                    for o in range(r, r + 49):
                        temp_pw += pw[o]

                    nums.append(pwd2[temp_pw])

                odd = nums[0] + nums[2] + nums[4] + nums[6]
                even = nums[1] + nums[3] + nums[5] + nums[7]
                result = odd * 3 + even

                if result % 10 == 0:
                    nlst[tc] += sum(nums)

            else:

                pass        # 길이비가 1 : 2 이상일 때

    print(f'#{tc}', nlst[tc])