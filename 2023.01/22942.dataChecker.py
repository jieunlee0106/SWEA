# ✨ 입력
import sys

input = sys.stdin.readline
N = int(input())
circle = []

# ✨ 준비
for i in range(N):
    a, b = map(int, input().split())
    circle.append((a - b, i))
    circle.append((a + b, i))

circle.sort()

# ✨ 비교
stack = []
for i in range(N * 2):
    d, c = circle[i]
    if len(stack) == 0:
        stack.append(circle[i])
    elif stack:
        if stack[-1][1] == c:
            stack.pop()
        else:
            stack.append(circle[i])
else:
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
# N = int(input())
# arr = []
# res = "YES"
# for _ in range(N):
#     if res == "NO":
#         break
#     else:
#         x, r = map(int, input().split())
#         mini, maxi = x-r, x+r
#         arr.append((mini, maxi))
#
#         for j in range(len(arr)-1):
#             c_mini, c_maxi = arr[j][0], arr[j][1]
#             if res == "NO":
#                 break
#             elif c_mini < mini < c_maxi and c_mini < maxi < c_maxi:
#                 pass
#             elif mini < c_mini and maxi < c_mini:
#                 pass
#             elif maxi > c_maxi and mini > c_maxi:
#                 pass
#             else:
#                 res = 'NO'
#
# print(res)