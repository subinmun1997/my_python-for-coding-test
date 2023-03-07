n, k = map(int, input().split())

count = 0
for x in range(n+1):
    for y in range(60):
        for z in range(60):
            if str(k) in str(x).zfill(2) + str(y).zfill(2) + str(z).zfill(2):
                count += 1

print(count)