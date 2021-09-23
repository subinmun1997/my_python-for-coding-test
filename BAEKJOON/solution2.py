n = int(input())
time = list(map(int, input().split()))
time.sort()

result = 0
total = 0
for t in time: # 1 2 3 3 4
    result = result + t
    total += result

print(total)