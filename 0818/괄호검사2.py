T = int(input())
for tc in range(1, T+1):
    sentence = input()
    l = len(sentence)
    stack = []
    result = 1
    for s in sentence:
        if s == '(' or s == '{':
            stack.append(s)
        elif s == ')' or s == '}':
            if len(stack)==0:
                result = 0
            elif s == ')' and stack.pop() == '{':
                result = 0
                break
            elif s == '}' and stack.pop() == '(':
                result = 0
                break
    if len(stack): # 빈 리스트인지 확인
        result = 0
    print(f'#{tc}', result)