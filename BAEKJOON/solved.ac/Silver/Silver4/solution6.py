n = int(input())
time = sorted(list(map(int, input().split())))

answer = 0
temp = 0
for i in time:
    temp += i
    answer += temp

print(answer)
