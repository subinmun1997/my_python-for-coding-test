n = int(input())
group = list(map(int, input().split()))
group.sort()

count = 0
people = 0

for g in group:
    people += 1
    if people >= g:
        count += 1
        people = 0
    else:
        continue

print(count)