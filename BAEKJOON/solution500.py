a, b = map(str, input().split())

answer = 0
for i in range(len(a)):
    for j in range(len(b)):
        answer += int(a[i]) * int(b[j])

print(answer)