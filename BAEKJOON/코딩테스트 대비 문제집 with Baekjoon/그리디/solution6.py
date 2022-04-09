n = int(input())
time = list(map(int, input().split()))
time.sort()

result = 0
temp = 0
for i in time:
    temp += i
    result += temp

print(result)