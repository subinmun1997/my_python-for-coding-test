n = int(input())

for i in range(n+1):
    s = str(i)
    temp = i

    for j in s:
        temp += int(j)
    if temp == n:
        print(i)
        break
else:
    print(0)