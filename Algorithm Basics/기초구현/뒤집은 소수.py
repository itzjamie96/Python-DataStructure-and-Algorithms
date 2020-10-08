'''
[뒤집은 소수]

N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요. 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면  23을  출력  한다. 단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
뒤집는 함수인 def reverse(x)  와  소수인지를  확인하는  함수  def  isPrime(x)를  반드시  작성하 여 프로그래밍 한다.

▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그  다음  줄에  N개의  자연수가  주어진다. 각 자연수의 크기는 100,000를 넘지 않는다.

▣ 출력설명
첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.

▣ 입력예제 1
5
32 55 62 3700 250

▣ 출력예제 1
23 73
'''
def reverse(num):
    result = ''
    numStr = str(num)
    for i in range(len(numStr)-1, -1, -1):
        result += numStr[i]

    return int(result)

def isPrime(num):

    #1은 소수가 아님
    if num == 1:
        return False

    # num//2+1 딱 절반까지 돌려도 충분히 약수는 확인가능
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True

N = int(input())
nList = list(map(int, input().split()))

for i in nList:
    # 먼저 숫자를 뒤집고
    rev = reverse(i)
    # 뒤집은게 소수면 프린트
    if isPrime(rev):
        print(rev, end=' ')

