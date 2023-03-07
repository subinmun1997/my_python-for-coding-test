n = int(input())

for i in range(1, n):
    sep = sum(int(i) for i in str(i))
    if i + sep == n:
        print(i)
        break
else:
    print(0)