def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

a, b = map(int, input().split())
if b > 10000000:
    b = 10000000
palindrome = [n for n in range(a, b+1) if str(n) == str(n)[::-1]]
for n in palindrome:
    if is_prime(n):
        print(n)

print(-1)