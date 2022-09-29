from itertools import combinations
def cook():
    pass
    for A, B in dish.items():
        ar, ac = A[0], A[1]
        br, bc = B[0], B[1]
        A_dish = arr[ar][ac] + arr[ac][ar]
        B_dish = arr[br][bc] + arr[bc][br]
        ret = abs(A_dish - B_dish)
        print(ret)

for tc in range(1, int(input())+1):
    n = int(input())
    lst= [i for i in range(n)]
    arr = [list(map(int, input().split())) for _ in range(n)]
    dish = {}
    for i in combinations(lst, n//2):
        if i not in dish:
            k = i
            v = []
            for j in lst:
                if j not in k:
                    v += [j]
            dish[k] = v
        cook()
    print(dish)