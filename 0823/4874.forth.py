for t in range(1, int(input())+1):
    data = list(input().split())
    stack = []
    for i in range(len(data)):
        if data[i] in '+-*/':
            num2 = stack.pop()
            if not stack:
                result = 'error'
                break
            elif stack:
                num1 = stack.pop()
            elif not stack:
                result = 'error'
                break
            if data[i] == '+':
                stack.append(num1+num2)
            elif data[i] == '-':
                stack.append(num1 - num2)
            elif data[i] == '*':
                stack.append(num1 * num2)
            elif data[i] == '/':
                if num2 == 0:
                    result = 'error'
                    break
                else:
                    stack.append(num1 / num2)

        elif data[i] == '.' :
            if len(stack) == 1:
                result = int(stack[0])
            else:
                result = 'error'
        else:
            stack.append(int(data[i]))

    print(f'#{t}', result)