# 요리사 문제 팁 그룹핑
n = 4
arr = [i for i in range(n)]

# 2그룹으로 나누고 싶다
def backtrack(k):

    if len(A) == n // 2:
        print(A, B + arr[k:])
        return
    if len(B) == n//2:
        print(A + arr[k:], B)
        return

    A.append(arr[k])
    backtrack(k + 1)
    A.pop()

    B.append(arr[k])
    backtrack(k + 1)
    B.pop()

A = [arr[0]]
B = []
backtrack(1)