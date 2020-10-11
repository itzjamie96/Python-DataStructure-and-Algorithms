'''
후위표기식 만들기

- 결과 스트링, 연산자 스택
- 숫자는 들어오는 족족 결과 스트링에 붙여주기
- 연산자가 들어오면:
    ( < */ < +-
    - 스택 탑이 현재 인풋보다 작으면 그냥 인풋 푸시
    - 스택 탑이 현재 인풋보다 같거나 크면 팝
    - (는 넣고 )가 나오면 (나올때까지 팝
        - (가 최상위인듯?
'''
import  sys

eq = sys.stdin.readline().rstrip()

order = {
    '*':1,
    '/':1,
    '+':2,
    '-':2,
    '(':0
}

stack = []
result = ''
i = 0

while i<len(eq):

    current = eq[i]

    if current.isdigit():
        result += current
        i += 1

    else:
        if len(stack) == 0:
            stack.append(current)
            i += 1

        else:

            if current == ')':
                if stack[-1] != '(':
                    result += stack.pop()
                else:
                    stack.pop()
                    i += 1

            # 탑의 우선순위가 나보다 낮으면(탑이 더 크면)
            # 그러면 맘놓고 현재 연산자 추가 (현재가 우선순위 더 큼)
            elif order[stack[-1]] > order[current]:
                stack.append(current)
                i += 1
            
            # 탑이랑 나랑 우선순위가 같으면 탑 빼기
            elif order[stack[-1]] <= order[current]:
                if stack[-1] != '(':
                    result += stack.pop()
                else:
                    stack.append(current)
                    i += 1

if len(stack)>0:
    result += ''.join(stack)

print(result)
