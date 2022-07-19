n = int(input())
number = list(map(int, input().split()))

def prime(num):
    for i in range(2, int(num ** 0.5)+1):
        if num%i == 0:
            return False
    return True

count = 0
for i in number:
    if i == 1:
        continue
    if prime(i):
        count += 1

print(count)