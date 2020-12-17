def getPowerSet(v):
    # 종료조건: N+1이 되면 현재 있는 부분집합의 요소들을 출력한다
    if v == N+1:
        for i in range(1, N+1):
            if inSet[i] == 1:
                print(i, end=' ')
        print()
        return
    
    else:
        inSet[v] = 1        # v가 부분집합에 포함됐을 때
        getPowerSet(v+1)    # v가 있는 상태에서 다른 요소들의 포함여부 확인하러 출발  
        inSet[v] = 0        # v가 부분집합에 없을 때
        getPowerSet(v+1)    # v가 없는 상태에서 다른 요소들의 포함여부 확인하러 출발


N = int(input())

# 부분집합 안에 요소가 있는지 없는지 확인용 리스트 inSet
# 1 ~ N까지이기 때문에 N+1을 곱해준다 (idx 0은 무시할거임)
inSet = [0] * (N + 1)

# 1부터 부분집합의 in/out 여부를 확인한다
getPowerSet(1)