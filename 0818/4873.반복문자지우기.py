T = int(input())
for t in range(T):
    str = list(input())
    stack = []
    for s in str:
        if not stack:
            stack.append(s)
        else:
            if s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)
    print(f'#{t+1}', len(stack))
