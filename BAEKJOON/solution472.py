n = int(input())

while True:
    mul_num = int(input())
    if mul_num == 0:
        break
    if mul_num % n == 0:
        print(f"{mul_num} is a multiple of {n}.")
    else:
        print(f"{mul_num} is NOT a multiple of {n}.")