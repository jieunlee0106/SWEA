for tc in range(1, int(input())+1):
    n, num = input().split()
    n = int(n)
    lst = []
    two = ''
    pwd = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
        '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
        'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    for i in range(n):
        lst.append(pwd[num[i]])

    for j in lst:
        two += j

    print(f'#{tc} {two}')