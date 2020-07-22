# 입력으로 주어진 문장에 모든 소문자 알파벳을 찾아 대문자로 변환한 다음,
# 그 결과를 출력하는 프로그램을 작성하라.

# 문장 입력받기
text = input()

# 변환한 결과물을 담을 empty str
result = ""

for i in text:
    
    # 현재 char가 소문자라면, -->> .islower()는 T/F로 나옴
    if i.islower():
        
        # 현재 char를 대문자로 변환한걸 result에 추가해라
        result += i.upper()
    
    # 이미 대문자거나 그냥 상관없는 문자면 그냥 result에 추가해라
    else:
        result += i

print(result)
