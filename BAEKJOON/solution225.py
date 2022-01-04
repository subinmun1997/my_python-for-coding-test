a = input() # 문서
b = input() # 검색하려는 단어

r = 0

while True:
    if (a.find(b) == -1):
        break
    a = a.replace(b, 'x', 1)
    r += 1

print(r)