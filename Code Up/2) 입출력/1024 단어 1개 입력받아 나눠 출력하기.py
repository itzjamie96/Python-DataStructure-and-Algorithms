# 단어를 1개 입력받는다.
# 입력받은 단어(영어)의 각 문자를
# 한줄에 한 문자씩 분리해 출력한다.

word = input()

for i in word:
    # print(f"'{i}'")  -->> 코드업에서는 fString이 안되나봄?!
    print("'",i,"'",sep="")

