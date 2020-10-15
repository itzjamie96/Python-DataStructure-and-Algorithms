import sys

# 전위순회로?
def powerset(n):

    if n == N+1:
        for i in range(N+1):
            if check[i] == 1:
                print(i, end=' ')
        print()
        # return

    else:
        # 요소 n이 있는 부분집합은 표시
        check[n] = 1
        powerset(n+1)   # left

        # 요소 n이 없는 부분집합
        check[n] = 0
        powerset(n+1)



N = int(sys.stdin.readline())
check = [0]*(N+1)
powerset(1)
