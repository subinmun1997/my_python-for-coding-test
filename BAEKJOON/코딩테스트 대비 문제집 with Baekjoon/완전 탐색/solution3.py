n = int(input())

result = 0
for i in range(n+1):
    result = i
    temp = str(i)
    for j in temp:
        result += int(j)
    if result == n:
        print(i)
        break
    if i == n:
        print(0)