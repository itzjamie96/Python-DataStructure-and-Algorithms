import sys

def sumOfsets(idx, currentSum ):

    # 현재 누적합이 전체합의 반보다 크면 그냥 불가
    if currentSum > total//2:
        return

    # 끝나는 경우: idx가 N이 되었을 때
    # idx: 0 ~ N-1
    if idx == N:
        if currentSum == total - currentSum:
            print("YES")
            sys.exit(0)     #프로그램이 종료됨! 이 함수가 아니라 이 파일이!

    else:
        # idx에 있는 원소 사용하는 경우
        sumOfsets(idx+1, currentSum+numList[idx])
        # idx에 있는 원소를 안쓰는 경우(sum에 포함 x)
        sumOfsets(idx+1, currentSum)



N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))

# 전체 합을 구한 후 전체합-부집합의합 = 부분집합의합 이 성립하는지 확인하면됨
total = sum(numList)

sumOfsets(0,0)
print("NO")