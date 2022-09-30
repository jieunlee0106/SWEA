
import math
def cal(s, k, idx):
    global ret

    if idx == N:
        ret += [s]
        return

    for j in range(4):
        if j == 0 and oper[j] != 0:
            oper[j] -= 1
            cal(s + nums[idx], k + 1, idx + 1)
            oper[j] += 1


        if j == 1 and oper[j] != 0:
            oper[j] -= 1
            cal(s - nums[idx], k + 1, idx + 1)
            oper[j] += 1


        if j == 2 and oper[j] != 0:
            oper[j] -= 1
            cal(s * nums[idx], k + 1, idx + 1)
            oper[j] += 1


        if j == 3 and oper[j] != 0:
            oper[j] -= 1
            cal(math.trunc(s / nums[idx]), k + 1, idx + 1)
            oper[j] += 1


for tc in range(1, int(input())+1):
    N = int(input())
    oper = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    ret = []
    cal(nums[0], 0, 1)
    mx = max(ret)
    mi = min(ret)
    print(f'#{tc} {mx - mi}')

