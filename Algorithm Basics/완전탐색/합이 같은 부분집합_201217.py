def sumOfSets(idx, currSum):
    global flag
    if flag == 1:   #flag가 1이면 바로 종료
        return
    
    if idx >= N:    #종료조건: 주어진 N개보다 커질 때 (=리스트 다 확인 했을 때)
        if total - currSum == currSum:  # 합-부분집합의 합 = 부분집합의 합인지 확인
            flag = 1
        return
    else:
        # currSum+nList[idx] << 이게 핵심 = idx번째 요소 포함여부를 이걸로 확인함
        sumOfSets(idx + 1, currSum + nList[idx])
        sumOfSets(idx+1, currSum)   #이건 포함 안하는거

N = int(input())
nList = list(map(int, input().split()))

flag = 0            # 종료 확인용 flag 변수
total = sum(nList)  # 부분집합의 합이 같은지 확인용 전체 합

sumOfSets(0,0)      # 시작idx = 0, 시작 currSum = 0

if flag == 1:
    print("YES")
else:
    print("NO")