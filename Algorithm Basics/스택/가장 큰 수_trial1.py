'''
가장 큰 수

선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하여
가장 큰 수를 만들라고 했습니다. 여러분이 현수를 도와주세요.(단 숫자의 순서는 유지해야 합니다)
만약 5276823 이 주어지고 3개의 자릿수를 제거한다면 7823이 가장 큰 숫자가 됩니다.

▣ 입력설명
첫째 줄에 숫자(길이는 1000을 넘지 않습니다)와 제가해야할 자릿수의 개수가 주어집니다.

▣ 출력설명
가장 큰 수를 출력합니다.

▣ 입력예제 1
5276823 3

▣ 출력예제 1
7823

▣ 입력예제 2
9977252641 5

▣ 출력예제 2
99776

- 나보다 작은 수가 내 앞에 있으면 안됨!
'''
N, M = map(int, input().split())        # 숫자, 제거할 숫자의 갯수
stack = []      # 비교 후 정답을 담을 스택

# 주어진 숫자를 str으로 만들어 각 자릿수를 확인할 수 있게 만든다
nList = str(N)

i = 0       # 자릿수 확인용 i
cnt = 0     # 몇번 pop했는지 확인할 cnt

# 모든 자릿수 확인할 때 까지 
while i<len(nList):
    
    # 모든 자릿수를 확인하기 전 주어진 M만큼 pop했을 때
    if cnt == M:
        stack.extend(nList[i:])     #남은 숫자들을 스택에 추가해준 후 break
        break

    # 스택이 비었을 때는 아묻따 추가
    if len(stack) == 0:  
        stack.append(nList[i])
        i += 1      # 추가한 후에는 자릿수를 이동해준다

    # 스택이 비지 않았을 때는 top이랑 비교 후 현재 값보다 작으면 pop
    elif int(stack[-1]) < int(nList[i]):
        stack.pop()
        cnt += 1    # pop 한 후에는 cnt 증가
    
    # 스택이 안비었고, top이 현재값보다 크면 추가
    else:
        stack.append(nList[i])
        i += 1      #자릿수 이동

# 끝까지 다 돌렸는데 아직 M만큼 pop을 안했다면 남은 횟수만큼 pop해주기
if cnt < M:
    for i in range(M-cnt):
        stack.pop()

print(*stack, sep='')

