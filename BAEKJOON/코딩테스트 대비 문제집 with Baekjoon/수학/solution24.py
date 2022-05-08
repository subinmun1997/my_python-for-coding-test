def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def add_square(num):
    result = sum(int(i)**2 for i in num)
    return result

def is_sangNum(num):
    pattern = []
    while num != 1:
        num = add_square(str(num))
        if num in pattern:
            return False
        pattern.append(num)
    return True


n = int(input())
for i in range(7, n+1):
    if is_prime(i) and is_sangNum(i):
        print(i)