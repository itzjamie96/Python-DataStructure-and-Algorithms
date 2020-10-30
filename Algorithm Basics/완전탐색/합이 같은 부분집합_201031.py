'''
numList = input list
n = length of numList

visited = 길이 n의 리스트
total = sum of numList

부분집합 구하기
- 종료조건: 현재 부분집합의 합 = total - 현재 부분집합의 합이면 YES
- 포함:
    visited[v] = 1
    f(다음합: numList[v]+numList[v+1])
- 안포함:
    visited[v] = 0
    f(다음합: numList[v])
6
1 3 5 6 7 10

'''
def sumOfPowerset(currSum, idx):
    global result

    if currSum == total - currSum:
        result = 'YES'
        return

    elif idx == n:
        return

    else:
        visited[idx] = 1
        sumOfPowerset(currSum+numList[idx], idx+1)

        visited[idx] = 0
        sumOfPowerset(currSum, idx+1)

n = int(input())
numList = list(map(int, input().split()))

visited = [0]*(n)
total = sum(numList)
result = ''
flag = 0
sumOfPowerset(0, 0)
if result == '':
    print("NO")
else:
    print(result)