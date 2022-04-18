t = int(input())

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for _ in range(t):
    n = int(input())
    while True:
        if check_prime(n):
            print(n)
            break
        else:
            n += 1
