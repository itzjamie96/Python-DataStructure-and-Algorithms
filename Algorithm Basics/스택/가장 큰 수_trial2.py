N, M = map(int, input().split())
nList = list(map(int, str(N)))      #입력받은 숫자를 list로 쪼개기

stack =  []     #정답을 담을 스택


for num in nList:

    # 스택이 비었고, M이 양수이면서 top이 현재 숫자보다 작으면 pop
    while stack and M>0 and stack[-1] < num:
        stack.pop()
        M -= 1  #한번 pop했으니 M은 감소

    # 저런 경우가 아니라면 그냥 추가!
    stack.append(num)

# 아직 M이 남았으면 그 갯수만큼 뒤에서부터 잘라야함
if M != 0:
    stack = stack[:-M]      # M개 만큼 자르기

print(*stack)
