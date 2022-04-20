n = int(input())

def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def palindrome(num):
    temp = str(num)[::-1]

    if int(temp) == num:
        return True
    else:
        return False

while True:
    if prime(n) and palindrome(n):
        print(n)
        break
    else:
        n += 1