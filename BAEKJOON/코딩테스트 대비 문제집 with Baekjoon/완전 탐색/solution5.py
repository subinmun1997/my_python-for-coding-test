n, k = map(int, input().split())

result = 0
for i in range(n+1):
    for j in range(60):
        for s in range(60):
            if str(k) in str(i)+str(j)+str(s):
                result += 1

print(result)