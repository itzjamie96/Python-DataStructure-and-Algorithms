'''
A+, A0, A-, B+, B-, C+, C0, C-, D0

총점 = 중간(35%) + 기말(45%) + 과제(20%)

- 각 학생의 총점을 구해서 순서대로 리스트에 넣는다
- 인덱스랑 함께 총점 기준으로 정렬한다
- N//10으로 정렬한 인덱스를 나눈다
'''
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for tc in range(1, T+1):

    N, K = map(int, input().split())

    scores = []
    for i in range(N):
        mid, fin, hw = map(int, input().split())

        scores.append(0.35*mid + 0.45*fin + 0.2*hw)

    result = [(score, idx+1) for idx, score in enumerate(scores)]
    result.sort(reverse=True)

    tmp = N//10
    ans = 0
    for i in range(N):
        if result[i][1] == K:
            ans = i//tmp

    print('#{} {}'.format(tc,grades[ans]))