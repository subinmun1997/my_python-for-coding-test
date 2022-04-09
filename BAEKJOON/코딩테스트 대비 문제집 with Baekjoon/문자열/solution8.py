n = int(input())

result = 0
for i in range(n):
    temp = ''
    array = []

    s = input()
    for j in s:
        if j != temp:
            array.append(j)
        temp = j

    if len(array) == len(set(s)):
        result += 1

print(result)
