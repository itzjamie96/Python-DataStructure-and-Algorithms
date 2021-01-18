for tc in range(10):
    n = int(input())
    find = input()
    text = list(input().split(find))    #특정 문자열을 기준으로 split한 후 
    print(f'#{n} {len(text)-1}')        #리스트의 길이에서 1을 뺀 값이 답