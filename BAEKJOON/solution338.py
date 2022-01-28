n = int(input())
tab = []

for _ in range(n):
    tab.append(int(input()))

count = 0
for i in range(n-1):
    count += tab[i] - 1

count += tab[n-1]
print(count)