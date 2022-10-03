# -------------------------
# used[] 전역 배열을 정수로 저장해서 매개변수로 전달
# -------------------------
arr = [10, 20, 30]
order = [0] * len(arr)

def perm(k, n, used):
    if k == n:
        print(order)
        return

    for i in range(n):
        if used & (1 << i): continue

        order[k] = arr[i]
        perm(k + 1, n, used | (1 << i))

perm(0, len(arr), 0)

