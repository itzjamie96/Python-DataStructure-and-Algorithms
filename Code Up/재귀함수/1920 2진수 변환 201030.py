'''
2진수로 바꾸기:
2의 나머지를 갖다 붙인다
'''
def toBinary(n):
    global result
    if n == 0:
        return result
    else:
        result = str(n%2)+result
        toBinary(n//2)

n = int(input())
result = ''
toBinary(n)
if result == '':
    print(0)
else:
    print(result)