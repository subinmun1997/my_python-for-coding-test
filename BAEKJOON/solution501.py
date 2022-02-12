computer = [0] * 101

n = int(input())
space = list(map(int, input().split()))

count = 0
for s in space:
    if computer[s] == 0:
        computer[s] = 1
    else:
        count += 1

print(count)