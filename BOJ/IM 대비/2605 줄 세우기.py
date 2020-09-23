'''
현재 인덱스에서 내용물을 뺀 위치로 이동하는 것
'''
N = int(input())
order = list(map(int, input().split()))

result = []
for i in range(len(order)):
    # 가야할 위치
    idx = i - order[i]
    
    # 그 위치에 값 넣기
    result.insert(idx, i+1)

print(*result)