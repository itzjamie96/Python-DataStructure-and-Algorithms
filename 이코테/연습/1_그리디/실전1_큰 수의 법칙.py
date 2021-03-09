'''
다양한 수로 이뤄진 배열이 있을 때 주어진 수들을 M번 더해서 가장 큰 수를 만든다
But, 배열의 특정 인덱스에 있는 숫자가 연속해서 K번 초과해서 더해질 수 없다

[input]
5 8 3
2 4 5 4 6
[output]
46
'''

N, M, K = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse=True)

result = 0
for i in range(1, M+1): # 0은 나머지도 0이라서 제외
    if i % K == 0:
        result += nums[1]
    else:
        result += nums[0]

print(result)

'''
리스트 정렬 (큰 수 ~ 작은 수)
for ~ M:
    if 현재 i가 K의 배수: 두번째 숫자 더하기
    else: 첫번째 숫자 더하기
'''