T = int(input())
for t in range(T):
    g = list(input())
    g_l = []
    stack = []
    result = 0
    for i in range(len(g)):
        if g[i] == '{' or g[i] == '}' or g[i] == '(' or g[i] == ')':
            g_l.append(g[i])

    if g_l[0] == '{' or g_l[0] == '(':
        for j in range(len(g_l)):
            if g_l[j] == '{' or g_l[j] == '(':
                stack.append(g_l[j])
            elif g_l[j] == '}':
                if stack[-1] == '{':
                    stack.pop()
                    result = 1
                else:
                    result = 0
                    break
            elif g_l[j] == ')':
                if stack[-1] == '(':
                    stack.pop()
                    result = 1
                else:
                    result = 0
                    break
        if stack:
            result = 0

    else:
        result = 0
    print(f'#{t+1}', result)

