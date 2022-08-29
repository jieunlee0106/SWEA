for t in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split()))
    bb = [0] * 11115
    man = [0] * 11115
    result = 0
    bbb = 'Possible'

    for i in range(m, 11115, m):
        bb[i] = k
    for k in range(n):
        man[lst[k]] -= 1

    for j in range(11115):
        result += bb[j]
        result += man[j]
        if result < 0:
            bbb = 'Impossible'
            break

    print(f'#{t}', bbb)

    '''
    def solve():
    n, m, k = map(int, input().split())
    li = list(map(int, input().split()))
    li.sort()
    for i in range(n):
        if (li[i] // m) * k < i+1:
            return 'Impossible'
    return 'Possible'
 
 
for T in range(int(input())):
    print(f'#{T+1} {solve()}')
    '''