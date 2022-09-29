from itertools import permutations
import math
def cal():
    global per
    mi = 10000
    mx = -10000
    for j in range(len(per)):
        s = nums[0]
        for i in range(N-1):
            if per[j][i] == '+':
                s += nums[i + 1]
            elif per[j][i] == '-':
                s -= nums[i + 1]
            elif per[j][i] == '*':
                s *= nums[i + 1]
            elif per[j][i] == '//':
                s = s / nums[i + 1]
                s = math.trunc(s)
        if s > mx:
            mx = s
        if mi > s:
            mi = s
    print(f'#{tc} {mx-mi}')

for tc in range(1, int(input())+1):
    N = int(input())
    temp = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    ret = []
    used = [0]*(N)
    oper = []
    oper += ['+'] * temp[0]
    oper += ['-'] * temp[1]
    oper += ['*'] * temp[2]
    oper += ['//'] * temp[3]


    per = set()
    for i in permutations(oper, N-1):
        per.add(i)
    per = list(per)
    cal()


