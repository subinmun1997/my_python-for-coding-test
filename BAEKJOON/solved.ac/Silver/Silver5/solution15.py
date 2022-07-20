n = int(input())
m = int(input())
prime = []

def check(num):
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

for i in range(n, m+1):
    if i == 1:
        continue
    if check(i):
        prime.append(i)

if prime:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)

