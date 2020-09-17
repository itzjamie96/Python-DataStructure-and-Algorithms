'''
1. 숫자카드를 딕셔너리로 받는다 (몇개인지 카운팅 위해)
2. key만 뽑아서 정렬된 리스트로 만듦
3. 이분탐색 함수 만들기
    - 만약에 숫자가 리스트안에 있으면 딕셔너리에서 value리턴
4. for문 돌려서 M 각각 함수에 넣기
'''

# 이분탐색 함수
def binarySearch(x):
    start = 0
    end = len(nList)-1

    while start <= end:
        mid = (start+end)//2

        if x > nList[mid]:
            start = mid+1

        elif x < nList[mid]:
            end = mid-1

        else:
            return nDict.get(x)
    return 0


# 숫자 카드들 받아서 정렬
N = int(input())
tmpList = list(map(int, input().split()))
tmpList.sort()

# 딕셔너리로 각각 몇개인지 확인 + 키만 따로
nDict = {}
nList = []
for i in tmpList:
    if i not in nDict:
        nDict[i] = 1
        nList.append(i)
    else:
        tmp = nDict[i]
        nDict[i] = tmp + 1

# 찾아야하는 숫자들 M
M = int(input())
mList = list(map(int, input().split()))

for i in mList:
    print(binarySearch(i), end=' ')