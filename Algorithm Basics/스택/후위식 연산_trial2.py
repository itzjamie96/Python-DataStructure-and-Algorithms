import sys

eq = sys.stdin.readline().rstrip()
stack = []

for current in eq:

    if current.isdigit():
        stack.append(int(current))

    else:
        if current == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)

        elif current == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)

        elif current == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)

        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(b//a)

print(stack[0])