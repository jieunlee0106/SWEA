n = int(input())
L = [0]*(n+1)
R = [0]*(n+1)
op = [0]*(n+1)  # 연산자+-*/
val = [0]*(n+1) # 피연산자

for _ in range(n):
    arr = input().split()
    idx = int(arr[0])
    if len(arr) == 4:   # 연산자
        op[idx] = arr[1]
        L[idx] = int(arr[2])
        R[idx] = int(arr[3])
    else:               # 피연산자
        val[idx] = int(arr[1])

def calc(v):

    # 피연산자인 경우 => 단말노드인 경우
    if L[v] == 0:
        return val[v]

    # 연산자인 경우 => 내부 노드
    else:
        l =calc(L[v])
        r = calc(R[v])
        # 후위 순회
        if op[v] == '+': return l + r
        elif op[v] == '-': return l - r
        elif op[v] == '*': return l * r
        elif op[v] == '/': return l / r


print(int(calc(1)))