import sys

'''
6
1 3 5 6 7 10
'''

def powerset(arr):

    for i in range(1<<N):

        currentSet = []
        for j in range(N):
            if i & (1<<j):
                currentSet.append(arr[j])

        tmp = []
        for k in arr:
            if k not in currentSet:
                tmp.append(k)

        if sum(tmp) == sum(currentSet):
            return "YES"
    return "NO"

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))
# print(numList)
print(powerset(numList))
