'''
문제가 웃긴다
왕자들끼리 눈치게임으로 공주 구할 사람을 고른다니 문제 읽고 잠시 쪼갰음

1. 1~N까지 enqueue
2. enqueue(dequeue) * 2
3. dequeue K번재
4. 한개 남을 때까지 반복
'''
import sys

def enqueue(data):
    Q.append(data)

def dequeue():
    return Q.pop(0)

N, K = map(int, sys.stdin.readline().split())

# 큐 만들기
Q = [i for i in range(1, N+1)]

# 한개 남을 때까지
while len(Q) > 0:

    # 앞에꺼 빼서 뒤에 넣고 * K-1번
    # K번째꺼는 그냥 빼버림
    for i in range(K-1):
        enqueue(dequeue())

    dequeue()

    if len(Q) == 1:
        print(Q[0])
        break

