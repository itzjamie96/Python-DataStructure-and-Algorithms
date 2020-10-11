import sys

eq = sys.stdin.readline().rstrip()
stack = []
result = ''

for current in eq:

    if current.isdigit():
        result += current

    else:
        if current == '(':
            stack.append(current)

        elif current == '*' or current == '/':

            while stack and (stack[-1] =='*' or stack[-1] == '/'):
                result += stack.pop()

            stack.append(current)

        elif current == '+' or current == '-':

            while stack and stack[-1] != '(':
                result += stack.pop()

            stack.append(current)

        elif current == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            
            # ( 빼기
            stack.pop()

while stack:
    result += stack.pop()

print(result)