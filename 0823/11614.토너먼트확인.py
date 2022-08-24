#홀수를 생각 못함
for t in range(1, int(input())+1):
    N = [0]*101
    n = int(input())
    card = list(map(int, input().split()))
    stack = []
    for i in range(1, n+1):
        N[i] = card[i-1]
    for j in range(1, n+1):
        if N[j] != 0:
            if not stack:
                if j == n:

                else:
                    stack.append(N[j])
                    idx = j
            elif stack:
                if stack[-1] == N[j]:
                    N[j] = 0
                    stack.pop()
                elif (stack[-1]==1 and N[j]==2) or (stack[-1]==2 and N[j]==3) or (stack[-1]==3 and N[j]==1):
                    N[idx] = 0
                    stack.pop()
                elif (stack[-1]==2 and N[j]==1) or (stack[-1]==3 and N[j]==2) or (stack[-1]==1 and N[j]==3):
                    N[j] = 0
                    stack.pop()
    for k in range(n+1):
        if N[k] != 0:
            result = k
    print(result)

