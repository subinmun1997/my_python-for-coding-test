n = int(input())
coin = sorted(list(map(int, input().split())))

answer = 1
for i in coin:
    if answer >= i:
        answer += i
    else:
        break

print(answer)