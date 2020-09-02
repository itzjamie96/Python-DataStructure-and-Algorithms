'''
[대표값]

N명의 학생의 수학성적이 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
답이 2개일 경우 성적이 높은 학생의 번호를 출력하세요. 만약 답이 되는 점수가 여러 개일 경우 번호가 빠른 학생의 번호를 답으로 한다.

▣ 입력설명
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 N개의 자연수가 주어진다. 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.

▣ 출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다. 평균은 소수 첫째 자리에서 반올림합니다.

▣ 입력예제 1
10
45 73 66 87 92 67 75 79 75 80

▣ 출력예제 1
74 7
'''
N = int(input())
scores = list(map(int, input().split()))

# 파이썬 round() = round_half_even = 정확하게 4.5000이럴때 짝수쪽으로 반올림 = 4
# 반올림을 위해 0.5를 더한후 int형으로 바꿔주자
avg = sum(scores)/N
avg = int(avg+0.5)

#아주 큰 정수 (정수형 가장 큰거 = 2의 31제곱)
mini = 2147000000

# enumerate: 탐색할 때 idx에는 index값을 반환해줌
for idx, score in enumerate(scores):
    tmp = abs(score - avg)  #평균과 점수 사이의 거리
    
    if tmp < mini:
        mini = tmp
        currentScore = score    #점수 같을 때 비교용
        ans = idx + 1      #학생 인덱스는 1부터 시작

    elif tmp == mini:       #거리가 같으면 점수가 더 큰 학생 고르기
        if score > currentScore:
            currentScore = score
            ans = idx + 1

print(avg, ans)