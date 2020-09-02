'''
[자릿수의 합]

N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력     하는 프로그램을 작성하세요. 각  자연수의  자릿수의  합을  구하는  함수를  def  digit_sum(x)를  꼭 작성해서 프로그래밍 하세요.

▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그  다음  줄에  N개의  자연수가  주어진다. 각 자연수의 크기는 10,000,000를 넘지 않는다.

▣ 출력설명
자릿수의 합이 최대인 자연수를 출력한다.

▣  입력예제 1
3
125 15232 97

▣  출력예제 1
97
'''
# 각 자릿수의 합을 리턴하는 함수
def digit_sum(num):
    num = str(num)
    sum = 0
    for i in num:
        sum += int(i)
    return sum

N = int(input())

# 숫자들 목록
Ns =list(map(int, input().split()))

max = 0     #최대 자릿수의 합을 담을 변수
ans = 0     #답은 숫자 그 자체!
for i in Ns:
    if digit_sum(i) > max:
        max = digit_sum(i)
        ans = i

print(ans)