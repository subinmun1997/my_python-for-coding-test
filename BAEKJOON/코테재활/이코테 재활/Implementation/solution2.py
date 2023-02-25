h = int(input())

count = 0
for x in range(h+1):
    for y in range(60):
        for z in range(60):
            if '3' in str(x)+str(y)+str(z):
                count += 1

print(count)