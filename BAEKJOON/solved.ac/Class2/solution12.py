n = int(input())
num = list(map(int, input().split()))

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

count = 0
for i in num:
    if is_prime(i):
        count += 1

print(count)