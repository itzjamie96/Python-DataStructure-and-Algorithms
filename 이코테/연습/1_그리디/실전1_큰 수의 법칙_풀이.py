'''
반복되는 수열을 찾아야함
(제일 큰수 * K + 두번째로 큰 수) <<== 이 조합이 몇개 있는지 찾기

(6+6+6+5)

수열의 반복 횟수 = M / (K+1) 번
--> 여기에 K를 곱하면 가장 큰 수가 나타나는 횟수가됨

M이 K로 나눠떨어지지 않는 경우: M % (K+1)
--> 남는 만큼 가장 큰 수를 더하면 됨

따라서 M/(K+1)*K + M%(K+1) = 가장 큰 수가 나타나는 전체 횟수

'''

N, M, K = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse=True)

first = nums[0]
second = nums[1]

cnt = int(M/(K+1)*K + M%(K+1))
result = cnt * first
result += (M - cnt) * second

print(result)