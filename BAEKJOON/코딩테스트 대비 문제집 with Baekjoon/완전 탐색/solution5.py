n, k = map(int, input().split())

result = 0
for i in range(n+1):
    if i < 10:
        i = '0' + str(i)
    for j in range(60):
        if j < 10:
            j = '0' + str(j)
        for s in range(60):
            if s < 10:
                s = '0' + str(s)
            if str(k) in str(i) + str(j) + str(s):
                result += 1

print(result)