n, m = map(int, input().split())

array = []
for _ in range(n):
    p, l = map(int, input().split())
    mileage = sorted(list(map(int, input().split())), reverse=True)
    if p >= l:
        array.append(mileage[l-1])
    else:
        array.append(1)

array.sort()
answer = 0
count = 0
for a in array:
    if answer + a <= m:
        answer += a
        count += 1

print(count)