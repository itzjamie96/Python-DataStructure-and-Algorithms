'''
- 10개의 숫자 중 min, max를 뺀 나머지의 평균 구하기
- 반올림은 소수점 첫째자리에서

- 리스트로 받아서 정렬한다
- 1번과 마지막꺼 뺀 값들의 합을 구한다
- 합 / 8 = 평균
'''

T = int(input())
for tc in range(1, T+1):
    nums = sorted(list(map(int, input().split())))

    sumV = sum(nums[1:9])
    avg = round(sumV/8)

    print('#{} {}'.format(tc,avg))
