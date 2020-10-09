import sys

# 문자열로 되어 있는 식을 계산해주는 함수
# ex: '10+5'를 넣으면 15를 리턴해줌
def add(string):
    # +가 있으면 그걸 기준으로 쪼개서 리스트로 담음
    tmp = list(map(int, string.split('+'))) 
    return sum(tmp) #합 리턴

# 받을 때 readline으로는 \n까지 받아서 그건 strip해줌
# 먼저 -를 기준으로 쪼갠다
# ex: ['55', '50+40']
eq = sys.stdin.readline().strip('\n').split('-')

# 결과 담을 변수
result = 0

# 쪼개진 eq의 첫번째는 무조건 더해져야한다
# ex: ['55', '50+40'] <= 여기에서 55는 무조건 더해져야함
result += add(eq[0])

# 첫번째를 제외한 애들은 빼줘야함
for i in range(1, len(eq)):
    result -= add(eq[i])

print(result)