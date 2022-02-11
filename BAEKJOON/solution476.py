e, f, c = map(int, input().split())

answer = 0
bottle = e+f
while bottle >= c:
    answer += bottle//c
    bottle = (bottle//c) + (bottle%c)

print(answer)