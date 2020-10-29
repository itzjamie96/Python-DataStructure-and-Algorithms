'''
오늘도 난..재귀함수를 연습하지

1~N까지 출력하는 재귀함수
- 젤 먼저 리턴되야하는게 1
- 그럼 종료 조건을 1로 두고 N-1을 호출해보자
- N-1 호출하고 끝나면 N을 프린트하는 방식
'''
def recur(N):
    if N == 1:
        print(N)
        return
    else:
        recur(N-1)
        print(N)

N = int(input())
recur(N)

