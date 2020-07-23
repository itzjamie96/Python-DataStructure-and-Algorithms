# 유니코드 출력

# utf-8이 깨지지 않게 utf-8로 인코딩 잊지 않기
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

print(u"\u250C\u252C\u2510")
print(u"\u251C\u253C\u2524")
print(u"\u2514\u2534\u2518")