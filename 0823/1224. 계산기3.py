for t in range(1, 11):

    def to_post(data):
        # 중위표기식
        # 연산자 - stack , 피연산자 - result
        # 우선 순위가 낮은 애들만 stack push
        isp = {'+': 1, '*': 2, '(': 0} # (는 스택 안에서는 우선 순위 낮게
        icp = {'+': 1, '*': 2, '(': 3}
        stack = []
        result = ''
        for i in range(len(data)):
            if data[i] in '+*()':
                if not stack:
                    stack.append(data[i])
                else:
                    # ) vs 나머지 : )는 스택에 안들어감
                    if data[i] == ')':
                        # 여는 괄호가 나올때 까지 pop하면서 연산자 출력, 여는 괄호는 pop하고 버리기
                        while stack[-1] != '(':
                            result += stack.pop()
                        stack.pop()  # 여는 괄호 버리기
                    else:  # +*( 인경우 / 스택top이 현재 읽는 데이터 보다 우선순위가 낮은 애가 나올 때 까지 result 로 옮기기
                        while stack and isp[stack[-1]] >= icp[data[i]]:
                            result += stack.pop()
                        stack.append(data[i])
            else:
                result += data[i]
        # 스택에 남아있는 연산자들 다 꺼내서 붙이기
        while stack:
            result += stack.pop()

        return result

    # 후위 표기식
    def calculate(data):
        # 피연산자 -  stack push
        # 연산자가 나오면, 피연산자 두 개 빼서 연산하고 다시 스택에 넣기
        stack = []
        for i in range(len(data)):
            if data[i] in '+*':
                num2 = stack.pop()
                num1 = stack.pop()
                if data[i] == '+':
                    stack.append(num1 + num2)
                elif data[i] == '*':
                    stack.append(num1 * num2)

            else:
                stack.append(int(data[i]))
        return stack.pop()

    n = int(input())
    print(f'#{t}', calculate(to_post(list(input()))))