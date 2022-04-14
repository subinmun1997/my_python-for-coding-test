def check(num):
    count = 0

    if num == 1:
        return False
    for i in range(2, num+1):
        if num%i == 0:
            count += 1
    if count > 1:
        return False
    else:
        return True

n = int(input())
numbers = list(map(int, input().split()))

result = 0
for number in numbers:
    if check(number):
        result += 1

print(result)

'''
# 더 좋은 방법
n = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    if number == 1:
        n -= 1
        continue

    for i in range(2, int(number**0.5)+1):
        if number%i == 0:
            n -= 1
            break

print(n)
'''