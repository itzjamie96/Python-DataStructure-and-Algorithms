'''
정수 n이 입력으로 들어오면 1부터 n까지의 합을 구하시오.

입력: 입력으로 자연수 n이 입력된다. (1<=n<=10,000)
출력: 1부터 n까지의 합을 출력한다.

[풀이]
- 1까지 계산해야하니 n이 0이 되면 종료
- sum(3) = 3 + 2 + 1
         = 3 + sum(2) ...
- 참고로 코드업에서 입력은 10,000까지만 한다고 했는 데 그 이상의 input들이 들어오며
최대 재귀를 넘었다는 에러가 떴다. 이것 때문에 재귀의 최대를 설정하는 모듈을 import했음
'''
import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

def sumN(n):
    if n>1:
        return n + sumN(n - 1)
    else:
        return 1

n = int(input())
print(sumN(n))