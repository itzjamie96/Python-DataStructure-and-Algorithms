import sys

T = int(sys.stdin.readline())
buttons = [300, 60, 10]     #분은 초단위로 바꿔준다

result = [0]*3
err = -1

for i in range(3):

    if T%buttons[i] == 0:
        result[i] = T//buttons[i]
        err = 0
        break

    else:
        result[i] = T // buttons[i]
        T = T%buttons[i]

        if T==0:
            break

if err == -1:
    print(err)
else:
    print(*result)

