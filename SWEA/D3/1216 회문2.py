def longestPalindrome(string):
    longest = ""
    for i in range(len(string)):
        # odd: left-i-right
        odd = checkPalindrome(string, i - 1, i + 1)
        if len(odd) > len(longest):
            longest = odd

        # even: i-right
        even = checkPalindrome(string, i, i + 1)
        if len(even) > len(longest):
            longest = even
    return len(longest)

def checkPalindrome(string, left, right):
    # left, right 모두 범위 안에 있고 두개가 같다면 계속 옆으로 확장
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1
    return string[left + 1:right]

for tc in range(10):
    t = int(input())
    board = [input() for _ in range(100)]

    maxi = 0
    for i in range(100):
        row = longestPalindrome(board[i])

        string = ""
        for j in range(100):
            string += board[j][i]
        col = longestPalindrome(string)

        tmp = max(row, col)
        if tmp > maxi:
            maxi = tmp

    print(f'#{t} {maxi}')

