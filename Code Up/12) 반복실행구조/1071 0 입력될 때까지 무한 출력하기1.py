# 정수가 순서대로 입력된다.
# -2147483648 ~ +2147483647, 단 개수는 알 수 없다.
#
# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
# while( ), for( ), do~while( ) 등의 반복문을 사용할 수 없다.


# list로 input 받기
numList = list(map(int,input().split()))

for n in numList:
    if n==0:
        break
    else:
        print(n)
