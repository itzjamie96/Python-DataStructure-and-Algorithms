import sys

eq = list(map(str, sys.stdin.readline().rstrip()))

i = 0
while i<len(eq):
    current = eq[i]

    if current.isdigit():
        i += 1

    else:
        if current == '+':
            tmp = int(eq[i-1]) + int(eq[i-2])
            eq.pop(i-1)
            eq.pop(i-2)
            eq[i-2] = str(tmp)
            i = i-2

        elif current == '-':
            tmp = int(eq[i - 2]) - int(eq[i - 1])
            eq.pop(i - 1)
            eq.pop(i - 2)
            eq[i-2] = str(tmp)
            i = i-2

        elif current == '*':
            tmp = int(eq[i - 2]) * int(eq[i - 1])
            eq.pop(i - 1)
            eq.pop(i - 2)
            eq[i-2] = str(tmp)
            i = i-2

        else:
            tmp = int(eq[i - 2]) // int(eq[i - 1])
            eq.pop(i - 1)
            eq.pop(i - 2)
            eq[i-2] = str(tmp)
            i = i-2

print(eq[0])