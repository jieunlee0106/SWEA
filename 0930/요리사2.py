def cook(k):
    global ret
    b = []
    if k == n:
        if len(A) == n//2:
            B = list(set(lst) - set(A))
            A_dish = 0
            B_dish = 0
            for ar in range(len(A)):
                for ac in range(len(A)):
                    if ar != ac:
                        A_dish += arr[A[ar]][A[ac]]
            for br in range(len(B)):
                for bc in range(len(B)):
                    if br != bc:
                        B_dish += arr[B[br]][B[bc]]
            abab = abs(A_dish - B_dish)
            ret = min(ret, abab)

    else:
        A.append(lst[k])
        cook(k + 1)
        A.pop()
        cook(k + 1)

for tc in range(1, int(input())+1):
    n = int(input())
    lst= [i for i in range(n)]
    arr = [list(map(int, input().split())) for _ in range(n)]
    A = [lst[0]]
    ret = 100000
    cook(1)
    print(f'#{tc} {ret}')