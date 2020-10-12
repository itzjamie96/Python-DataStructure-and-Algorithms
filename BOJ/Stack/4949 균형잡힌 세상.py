'''
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다. << 먼소리여

[가 들어온다 => top이 ]가 아니면 no
(가 들어온다 => top이 )가 아니면 no
인풋의 끝은 .

텍스트가 끝이 없어서 while로 받아야한다

이거 다시 풀어보기
'''
import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    # print(sentence)
    if sentence == '.':
        break

    stack = []

    for current in sentence:

        if current == '(' or current == '[':
            stack.append(current)

        elif current == ')':
            if (len(stack) == 0 or stack[-1] != '('):
                print('no')
                break

            elif stack[-1] == '(':
                stack.pop()

        elif current == ']':
            if (len(stack) == 0 or stack[-1] != '['):
                print('no')
                break
            elif stack[-1] == '[':
                stack.pop()

        elif current == '.':
            if len(stack) > 0:
                print('no')
                break
            else:
                print('yes')
                break
    else:
        break




