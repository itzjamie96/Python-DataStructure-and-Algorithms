# 년월일이 '.'(닷)으로 구분되어 입력된다.
# 일월년으로 바꾸어 '-'(대쉬, 마이너스)로 구분해 출력한다.
# (단, 한 자리 일/월은 0을 붙여 두자리로, 년도도 0을 붙여 네자리로 출력한다.)

y,m,d = map(str,input().split("."))

if len(y)<4:
    y = "0"*(4-len(y)) + y

if int(m)<10 and len(m)<2:
    m = "0"+m

if int(d)<10 and len(d)<2:
    d = "0"+d

print(d,m,y,sep="-")