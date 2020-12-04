T = int(input())
for tc in range(1, T+1):

    N = int(input())
    result = [[1]]

    for i in range(1, N):
        row = [1]
        for j in range(len(result[-1])-1):
            sumV = 0
            for k in range(2):
                sumV += result[-1][j+k]
            row.append(sumV)
        row.append(1)
        result.append(row)

    print('#{}'.format(tc))
    for i in range(len(result)):
        print(*result[i])