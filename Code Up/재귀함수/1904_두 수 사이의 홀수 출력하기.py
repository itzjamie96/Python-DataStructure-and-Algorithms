'''
시작수(a)와 마지막 수(b)가 입력되면 a부터 b까지의 모든 홀수를 출력하시오.

입력: 두 수 a, b 가 입력된다. (1<=a<=b<=100)
출력: a~b의 홀수를 모두 출력한다.

[풀이]
- a와 b 모두 홀수일 수 있으니 둘다 홀수인지 판별할 수 있도록 마지막에 a가 b+1이 되었을 때 종료시킴
- a가 홀수라면 a를 출력하고, if문을 나와서 무조건 a+1, b로 재귀로 부름
'''
def odd(a, b):
    if a == b+1:
        return
    else:
        if a%2:
            print(a, end=' ')
        odd(a+1, b)

a, b = map(int, input().split())
odd(a, b)