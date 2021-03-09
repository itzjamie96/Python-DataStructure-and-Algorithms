'''
여러 숫자 카드 중 가장 큰 숫자가 있는 카드 뽑기
규칙:
- N * M 형태
- 뽑으려는 카드가 있는 row 선택
- row에서 가장 작은 숫자 카드 선택
'''
N, M = map(int, input().split())

result = 0
# 각 row를 입력받을 때마다 min을 찾고, 그 중 max를 구한다
for i in range(N):
    tmp = list(map(int, input().split()))
    current_min = min(tmp)
    if current_min > result:
        result = current_min

print(result)

'''
3 3
3 1 2
4 1 4
2 2 2
=== 2
2 4
7 3 1 8
3 3 3 4
=== 3

'''