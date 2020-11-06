'''
1. 만약 {이나 (가 있으면 스택에 넣어준다
2. }가 들어오면
    - 스택의 top이 {가 아니면 바로 리턴 0
    - 스택의 top이 {면 스택을 팝한다
3. )도 }랑 똑같이 한다
4. 만약 스택에 뭐가 남아있으면 짝이 없는 것이기 때문에 리턴 0
5. 그동안 강제 리턴이 없었고 스택에 남은게 없으면 리턴 1
'''
def isPair(string):

    stack = []
    for element in string:
        if element == '{' or element == '(':
            stack.append(element)

        elif element == '}':
            if len(stack)>0 and stack[-1] == '{':
                stack.pop()
            else:
                return 0

        elif element == ')':
            if len(stack)>0 and stack[-1] == '(':
                stack.pop()
            else:
                return 0

    if len(stack) > 0:
        return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):

    string = input()

    print('#{} {}'.format(tc, isPair(string)))
