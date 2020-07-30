"""
연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.

22220228 -> 2222/02/28

해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면 [그림1]과 같이 ”YYYY/MM/DD”형식으로 출력하고, 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.

[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다. 다음 줄부터 각 테스트 케이스가 주어진다.

[출력]

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

# test case 갯수 입력받기
T = int(input())

# test case 갯수 만큼 for문 돌림
for case in range(T):

    #날짜를 str타입으로 받는다
    date = input()

    # 유효하지 않은 경우
    # 월이 1~12가 아님
    if int(date[4:6]) < 1 or int(date[4:6]) > 12:
        print(f"#{case+1}",-1, sep=" ")

    # 1,3,5,7,8,10,12월은 31일까지
    elif int(date[4:6]) in [1,3,5,7,8,10,12] and int(date[6:8])>31:
        print(f"#{case+1}", -1, sep=" ")

    # 4,6,9,11월은 30일까지
    elif int(date[4:6]) in [4,6,9,11] and int(date[6:8])>30:
        print(f"#{case+1}", -1, sep=" ")

    #2월은 28일까지
    elif int(date[4:6]) == 2 and int(date[6:8]) > 28:
        print(f"#{case+1}", -1, sep=" ")

    else:
        print(f"#{case+1} {date[:4]}/{date[4:6]}/{date[6:]}")