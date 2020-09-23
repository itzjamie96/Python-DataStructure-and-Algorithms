# 난쟁이 리스트 입력받기
dwarves = [int(input()) for _ in range(9)]

# 우선 있는 난쟁이들의 합을 구함
total = sum(dwarves)

# 뺄 난쟁이들
d1 = d2 = 0
flag = True     #혹시 일찍 break하고 싶을 때를 위해

for i in range(len(dwarves)):
    if flag == False:
        break
        
    # 난쟁이 2명 뺐을 때 100이면 걔네 알아뒀다가 나중에 빼기
    for j in range(1, len(dwarves)):
        if total - (dwarves[i] + dwarves[j]) == 100:
            d1 = dwarves[i]
            d2 = dwarves[j]
            flag = False

# 거짓 난쟁이들 빼기
dwarves.remove(d1)
dwarves.remove(d2)

# 정렬 후 프린트!
dwarves.sort()
print(*dwarves, sep='\n')