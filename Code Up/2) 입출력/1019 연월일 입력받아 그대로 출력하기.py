# 년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자.
# 입력: 연, 월, 일이 ".(닷)"으로 구분되어 입력된다.
# 출력: 입력받은 연, 월, 일을 yyyy.mm.dd 형식으로 출력한다. (한 자리 수는 앞에 0을 붙여 출력)

year, month, day = map(str, input().split("."))

# test case 중 99.1.1 같은 경우도 있기 때문에 각 입력값의 길이 확인 후 0 추가 필요

if len(year) < 4:
    year = "0" * (4-len(year)) + year

if int(month)<10 and len(month)<2:
    month = "0"+month

if int(day)<10 and len(day)<2:
    day = "0"+day

print(year, month, day, sep=".")
