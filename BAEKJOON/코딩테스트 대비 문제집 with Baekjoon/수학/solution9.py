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