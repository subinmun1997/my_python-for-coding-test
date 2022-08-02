def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

while True:
    n = int(input())
    count = 0
    if n == 0:
        break
    for i in range(n+1, 2*n+1):
        if prime(i):
            count += 1
    print(count)